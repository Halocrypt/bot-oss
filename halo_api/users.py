from halo_api.constants import build_url
from . import auth


class Users(object):
    def __init__(self, auth: auth.Auth) -> None:
        self.auth = auth

    def user_details(self, user):
        return self.auth.get(build_url(f"/accounts/{user}"))["data"]["user_data"]

    def disqualify(self, user, reason, points):
        return self.auth.patch(
            build_url(f"/admin/accounts/{user}/disqualify"),
            json={"reason": reason, "points": points},
        )["data"]

    def requalify(self, user):
        return self.auth.patch(build_url(f"/admin/accounts/{user}/requalify"))["data"]

    def get_all_users(self, event="main"):
        return self.auth.get(build_url(f"/admin/{event}/users/"))["data"]
