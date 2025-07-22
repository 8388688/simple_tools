from random import randrange, choice, randint, random
from typing import Sequence

from simple_tools.misc import deprecated

__all__ = ['random_choice_old', "random_pop", "random_choice"]


def create_random_list(start_=0, end_=10, step_=1, values: Sequence = ()):
    import warnings
    warnings.warn(f"f{deprecated(create_random_list)} 将在 3.9 版本移除",
                  DeprecationWarning, stacklevel=4)
    """生成随机数列

    生成一个随机数列，或把现有的数列打乱

    :param start_: 起始值
    :param end_: 结束值(终止值)
    :param step_: 步长
    :param values: 默认为 None，如果你想要打乱现有的数列，就修改成一个可迭代序列，
     注：当这个参数不为 None 时则直接忽略 start_, end_, step_ 三个参数
    :return: 当 returns 为 True 时返回乱序的数列，否则返回 0
    """
    list1 = lists = []  # 列表元素初始化
    if not values:
        # for 生成有序的数列
        for i in range(start_, end_, step_):
            lists.append(i)  # 在数列的末尾增添元素
    # 把lists里的元素随机分布到 list1 里
    else:
        for i in values:
            lists.append(i)
    for i in range(len(lists)):
        random1 = randrange(0, len(lists), 1)  # 随机生成一个lists的下标
        list1.append(lists.pop(random1))
    return list1


def random_choice_old():
    return choice([True, False])


def random_choice(seq, permission):
    print(
        f"\033[0;31m要访问旧版本的 random_choice 函数，请调用 {random_choice_old.__name__}()\033[0m")
    rd_choice = random()
    pg = permission
    sum_ = 0
    pg_new = []
    for i in pg:
        pg_new.append(sum_)
        sum_ += i
    pg_new = list(map(lambda x: x / sum_, pg_new))
    for i in range(len(pg_new) - 1, -1, -1):
        if pg_new[i] <= rd_choice:
            # print(rd_choice, "=>", g[i])
            # print(i, "=>", dg[i])
            # break
            return seq[i]


def random_pop(*args, filters=None):
    base_value = list(args)
    for a000 in range(0, len(base_value), 1):
        yield base_value.pop(randint(0, len(base_value) - 1))
