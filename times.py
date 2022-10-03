from time import time, localtime, strftime, sleep
from module1.data_base import NULL, null

__all__ = ['get_false_unix_time', 'wait']


def get_false_unix_time(v_time=time()):
    return strftime('%Y%m%d%H%M%S', localtime(v_time))


def wait(seconds=null, busy_loop=NULL):
    """等待

    具体略

    :param seconds: 等待的秒数
    :param busy_loop: 精确等待，默认为 NULL(自动判断)，
    \n 如果 busy_loop 为 True，则精确更新，如果为 False，则只用 sleep() 函数
    \n 当 busy_loop 被启用时，如果 seconds 的值很大，将会非常占用系统资源，所以一般不建议启用 busy_loop
    """
    cache_times = time()
    if busy_loop is NULL:
        if seconds == null:
            pass
        elif seconds < 0.01:
            while time() - cache_times < seconds:
                pass
        else:
            sleep(seconds)
    elif busy_loop:
        while time() - cache_times < seconds:
            pass
    else:
        sleep(seconds)
    return seconds
