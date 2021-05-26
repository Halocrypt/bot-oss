from halo_api.constants import build_url
from . import auth


class Play(object):
    def __init__(self, auth: auth.Auth) -> None:
        self.auth = auth

    def get_top_players(self, event):
        return self.auth.get(build_url(f"/play/{event}/leaderboard"))["data"][:20]

    def get_user_count(self, event):
        return self.auth.get(build_url(f"/admin/{event}/user-count/"))["data"]["count"]

    def get_answer(self, event, question_number):
        ret = [
            x
            for x in self.auth.get(build_url(f"/admin/events/{event}/questions/"))[
                "data"
            ]
            if x["question_number"] == int(question_number)
        ]
        return ret[0]["_secure_"]["answer"] if ret else None
