from time import time as timestamp1
import tkinter

from simple_tools.data_base import ST_WORK_SPACE, NULL, money, cacheTimes, fp
from simple_tools.system_extend import generate_file_path, delete

# from tkinter import simpledialog

__all__ = ['clear_module_cache', 'receive', ]


def clear_module_cache():
    delete(ST_WORK_SPACE)


def receive(cm1=NULL):
    """领取离线收益

    这个函数是我在玩消灭病毒的时候，有感而发写的

    :param cm1: comment1
    :return: void
    """
    global cacheTimes, money
    money += int(timestamp1() - cacheTimes)
    print('\n', cm1, '+', int(timestamp1() - cacheTimes))
    if abs(cacheTimes - timestamp1()) >= 1:
        cacheTimes = timestamp1()
