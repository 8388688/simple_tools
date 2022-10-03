import os
from time import time, sleep
from module1 import NULL, null

__all__ = ['breakpoint_', 'pass_']


def pass_(returns=null):
    """没用的函数

    :return: returns
    """
    return returns


def breakpoint_(values=0, func=pass_, exit_=False, comment='Press any key to continue:'):
    """退出

    让程序暂停，以便自己或其他的程序猿）查看运行结果

    :param values: exit()中的值，0表示正常退出，非0表示在退出前，发生了不该发生的事情
    :param func: 函数
    :param exit_: 是否退出
    :param comment: 提示文本
    :return: void
    """
    print(comment, end='')
    os.system('pause>nul')
    func()
    if exit_:
        exit(values)
    return values
