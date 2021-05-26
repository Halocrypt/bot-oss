from halo_api.constants import build_url
import requests


class Auth(object):

    _access_token: str
    _refresh_token: str

    def _request_proxy(self, method, *args, **kwargs) -> dict:
        if not self._access_token:
            raise Exception("you aren't logged in!")
        default_headers = {
            "Authorization": f"Bearer {self._access_token}",
            "x-refresh-token": self._refresh_token,
        }
        headers = kwargs.get("headers", {})
        headers = {**headers, **default_headers}
        kwargs["headers"] = headers
        req = getattr(requests, method)(*args, **kwargs)
        try:
            js = req.json()
            error = js.get("error")
            if error == "refresh":
                resp = requests.get(
                    build_url("/accounts/token/refresh"), headers=default_headers
                )

                err = resp.json().get("error")
                message = f"Could not refresh token automatically, please log in again!\n\
                Server said\n{err}"
                if err:
                    raise Exception(message)
                self._access_token = resp.headers.get("x-access-token")
                self._refresh_token = resp.headers.get("x-refresh-token")

                return self._request_proxy(method, *args, **kwargs)
            if error:
                raise ValueError(error)
            return js
        except ValueError:
            raise
        except Exception as e:
            print(e)
            return req

    def patch(self, url, *args, **kwargs):
        return self._request_proxy("patch", url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return self._request_proxy("post", url, *args, **kwargs)

    def get(self, url, *args, **kwargs):
        return self._request_proxy("get", url, *args, **kwargs)

    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password

    def login(self):
        ret = requests.post(
            build_url("/accounts/login"),
            json={"user": self.user, "password": self.password},
        )
        if not ret.ok:
            raise Exception(
                f"Authentication error!\n Server said:\n{ret.json()['error']}"
            )

        resp = ret.json()["user_data"]
        user = resp["user"]
        name = resp["name"]
        print(f"Logged in as {user} ({name})")
        self._access_token = ret.headers.get("x-access-token")
        self._refresh_token = ret.headers.get("x-refresh-token")
        return self
