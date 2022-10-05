from tkinter.messagebox import showerror, showinfo, showwarning

import turtle
from random import randrange
import tkinter

from simple_tools.data_base import NULL
from simple_tools.times import wait

__all__ = ['bomb1', 'bomb2', 'create_toplevel', 'draw1', 'draw2']


def bomb1(number=20):
    for a000 in range(number):
        showerror(title='ERROR', message=str(a000))
        showwarning(title='WARNING', message=str(a000))
        showinfo(title='INFO', message=str(a000))


def bomb2(number=20, tips=True, title_='WARNING', msg_='系统显示，你脑子可能进水了'):
    if tips:
        showwarning(title=title_, message=msg_)
    for a000 in range(number + 1):
        for a001 in range(a000):
            showinfo(title='INFO', message=str(a001 + 1))
            showerror(title='ERROR', message=str(a001 + 1))
            showwarning(title='WARNING', message=str(a001 + 1))


def create_toplevel(title_='text', text_=' Hello, world!', xu_hua=0.5, top_most=0):
    top = tkinter.Toplevel()
    top.wm_title(title_)
    top.attributes('-alpha', xu_hua)
    top.attributes('-topmost', top_most)
    msg1 = tkinter.Message(top, text=text_)
    msg1.pack()


def draw1(right_=True, pencolor_='green', fillcolor_='red', max_=200, steps=12, clear_=False):
    """画三角形

    :param right_: True表示向右转，False表示向左转
    :param pencolor_: 画笔颜色
    :param fillcolor_: 填充颜色
    :param max_: 画 （max / steps） 个三角形
    :param steps: 第n个三角形相较于第n-1个三角形的大小（即步长值）
    :param clear_: 是否清屏，默认为 False

    :return: void
    """
    if clear_:
        turtle.clear()
    a = turtle.Turtle()
    a.color(pencolor_, fillcolor_)
    a.pensize(3)
    length = 10
    while length <= max_:
        a.begin_fill()
        for a000 in range(0, 3):
            a.forward(length)
            if right_:
                a.right(120)
            else:
                a.left(120)
        a.speed(length / 20)
        a.end_fill()
        a.left(10)
        length += steps
    wait(2)


def draw2(yuan_length, max_, fd, angle, colors=NULL):
    """画多边形

    画（180/(180-n)）边形

    :param yuan_length: 原长度
    :param max_: 最大值， 即多边形的边长
    :param fd: 幅度
    :param angle: 角度：（180/(180-n)）
    :param colors:  强制使用某种颜色，NULL表示随机（建议将此参数设置为NULL）
    :return: void
    """
    a = turtle.Turtle()
    color_ = ('red', 'yellow', 'green', 'blue', 'black', 'brown', 'white', 'orange', 'pink', 'purple', 'grey')
    length = yuan_length
    while length < max_:
        a.forward(length)
        a.right(angle)
        length += fd
        a.speed(length / 20)
        if colors is NULL:
            random1 = randrange(0, len(color_))
            a.pencolor(color_[random1])
        else:
            a.pencolor(colors)
