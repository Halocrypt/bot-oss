from constants import TEAM_HALO


def is_team_halo(ctx):
    return any(str(x.id) == str(TEAM_HALO) for x in ctx.author.roles)
