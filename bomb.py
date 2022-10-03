from tkinter import messagebox as msg

__all__ = ['bomb1', 'bomb2']


def bomb1(number=20):
    for a000 in range(number):
        msg.showerror(title='ERROR', message=a000)
        msg.showwarning(title='WARNING', message=a000)
        msg.showinfo(title='INFO', message=a000)


def bomb2(number=20, tips=True, title_='WARNING', msg_='系统显示，你脑子可能进水了'):
    if tips:
        msg.showwarning(title=title_, message=msg_)
    for a000 in range(number + 1):
        for a001 in range(a000):
            msg.showinfo(title='INFO', message=a001 + 1)
            msg.showerror(title='ERROR', message=a001 + 1)
            msg.showwarning(title='WARNING', message=a001 + 1)
