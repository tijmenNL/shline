# Basic theme which only uses colors in 0-15 range

class Color(DefaultColor):
    USERNAME_FG = 8
    USERNAME_BG = 15
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    CWD_FG = 15 # white
    CWD_BG = 8 # dark grey

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2  # green
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 1  # red
    REPO_DIRTY_FG = 15 # white

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 8
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0
