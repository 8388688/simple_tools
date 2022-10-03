import os
from time import time as time_
import tkinter.simpledialog
import tkinter

from module1.data_base import NULL, money, cacheTimes, fp
from module1.system_ import get_file_name_of_generator

# from tkinter import simpledialog

__all__ = ['createToplevel', 'receive', ]


def createToplevel(title_='text', text_=' Hello, world!', xu_hua=0.5, top_most=0):
    top = tkinter.Toplevel()
    top.wm_title(title_)
    top.attributes('-alpha', xu_hua)
    top.attributes('-topmost', top_most)
    msg1 = tkinter.Message(top, text=text_)
    msg1.pack()


def receive(cm1=NULL):
    """领取离线收益

    这个函数是我在玩消灭病毒的时候，有感而发写的

    :param cm1: comment1
    :return: void
    """
    global cacheTimes, money
    money += int(time_() - cacheTimes)
    print('\n', cm1, '+', int(time_() - cacheTimes))
    if abs(cacheTimes - time_()) >= 1:
        cacheTimes = time_()


if __name__ == '__main__':
    fp = '..\\'
    k = []
    for i in get_file_name_of_generator(fp, False):
        try:
            k.append(i.split('.')[-1])
        except:
            print(k)
        finally:
            print(i)
    k = sorted(list(set(k)))
    print(k)
