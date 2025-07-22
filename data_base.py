from os import getcwd, getenv
from os.path import join

fp = getcwd()

ST_WORK_SPACE = join(str(getenv("APPDATA")), "simple_tools")

science_tuple = ("", "K", "M", "B", "T", "P", "E", "Z", "Y", "S", "L", "X", "D", "C", "H", "I", "N", "A", "F", "G",
                 "J", "O")

tabs_bl = (("└─", "   "), ("├─", "│  "))

tabs = (("┌", "┬", "┐", "├", "┼", "┤", "└", "┴", "┘",),
        ("╔", "╦", "╗", "╠", "╬", "╣", "╚", "╩", "╝",),
        ("┏", "┳", "┓", "┣", "╋", "┫", "┗", "┻", "┛",),
        ("│", "╳", "┃", " ", "╭", "─", "╮", "╰", "━", "╯",),)


def pass_(returns=0, *args, **kwargs):
    """没用的函数

    @return: returns
    """
    if kwargs.get("quiet", False):
        print(args)
        print(kwargs)
    return returns


__all__ = [
    "ST_WORK_SPACE",
    "fp", "science_tuple", "tabs", "tabs_bl",
    "pass_"
]
