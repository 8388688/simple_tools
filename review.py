def bl(value, sep=':', line_sign=0, lines=False, all_values=False):
    """bl是遍历的意思

    注：这里的bl只是“遍历”的首字母缩写，与原耽无关
    :param value: 判断输入的是什么类型
    :param sep: 第 n 项和第 n+1 项之间的分隔符
    :param line_sign: 加行号标志
    :param lines: 空行，默认为 False
    :param all_values: 全部遍历
    :return: void
    """
    count = 0
    if type(value) == dict:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                bl(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=all_values)
            elif line_sign:
                count += 1
                print(str(count) + sep + str(a000) + sep + str(value[a000]))
            else:
                print(str(a000) + sep + str(value[a000]))
    elif type(value) == str or type(value) == list or type(value) == tuple or type(value) == set:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                bl(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=all_values)
            elif line_sign:
                count += 1
                print(count, sep, str(a000), sep='')
            else:
                print(a000)
    # elif type(value) == __generator:
    else:
        print('输入类型不正确')
        return 1


def bl_of_generator(*args):
    # 以下代码画出制表线，根节点即parent为空，不需要制表符
    val = args
    if val:
        lines = ''
        # 以下画出这个节点上层节点的制表符
        for node in val:
            if node != node.parent.children[-1]:
                lines += '│ '
            else:
                lines += '  '
        # 以下画出这个紧邻节点前的制表符
        if self.parent.children[-1] == self:
            # 如果当前打印的节点已经是同级最后一个节点，线条就不向下延伸
            lines += '└─'
        else:
            lines += '├─'  # 默认还可以向下延伸
        print(lines, end='')
    print(data)  # 打印出数据
    # 如果存在子节点，那么就递归打印
    for subTreeNode in self.__children:
        bl_of_generator()  # 调用递归函数


def review(value, sep=':', line_sign=0, lines=False, all_values=True, deep=0, decorate=True):
    """review是检视的意思，它的作用等价于bl

    :param line_sign: 加行号标志
    :param value: 判断输入的是什么类型
    :param sep: 第n项和第n+1项之间的分隔符
    :param lines: 空行，默认为 False
    :param all_values: 全部遍历
    :param deep: 递归深度，不要更改这个参数
    :param decorate: 装饰
    :return: void
    """

    count = cache_count = 0
    deeps = deep
    if type(value) == dict:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                review(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=all_values, deep=deep + 1,
                       decorate=decorate)
            elif line_sign:
                count += 1
                print(str(count) + sep + str(a000) + sep + str(value[a000]))
            elif decorate:
                if a000 == value[-1]:
                    print('├ ' * (deeps - 1) + '└ ', str(a000) + sep + str(value[a000]), sep='')
                else:
                    print('├ ' * deeps, str(a000) + sep + str(value[a000]), sep='')
            else:
                print(str(a000) + sep + str(value[a000]))
    elif type(value) == str or type(value) == list or type(value) == tuple or type(value) == set:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                review(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=all_values, deep=deep + 1,
                       decorate=decorate)
            elif line_sign:
                count += 1
                print(count, sep, str(a000), sep='')
            elif decorate:
                if a000 == value[-1]:
                    print('├ ' * (deeps - 1) + '└ ', a000, sep='')
                else:
                    print('├ ' * deeps, a000, sep='')
            else:
                print(a000)
    else:
        print('输入类型不正确')
        return 1
    del cache_count


def review_2(value, sep=':', line_sign=0, lines=False, _all=True, deep=0, decorate=True, dict_sign=':'):
    """review是检视的意思，它的作用等价于bl

    line_sign 和 decorate 互相冲突，line_sign 的优先级高于 decorate
    检视优先级中，dictionary 的优先级为 1，list，tuple，set，str 的优先级为 2，其他类型的优先级为 3

    :param line_sign: 加行号标志
    :param value: 判断输入的是什么类型
    :param sep: 第n项和第n+1项之间的分隔符
    :param lines: 空行，默认为 False
    :param _all: 全部遍历
    :param deep: 递归深度，不要更改这个参数
    :param decorate: 装饰
    :param dict_sign: 字典分隔符
    :return: void
    """
    count = cache_count = 0
    deeps = deep
    if type(value) == dict:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                review(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=_all, deep=deep + 1,
                       decorate=decorate)
            elif line_sign:
                count += 1
                print(str(count) + sep + str(a000) + dict_sign + str(value[a000]))
            elif decorate:
                if a000 == value[-1]:
                    print('├ ' * (deeps - 1) + '└ ', str(a000) + dict_sign + str(value[a000]), sep='')
                else:
                    print('├ ' * deeps, str(a000) + dict_sign + str(value[a000]), sep='')
            else:
                print(str(a000) + dict_sign + str(value[a000]))
    elif type(value) == str or type(value) == list or type(value) == tuple or type(value) == set:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                review(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=_all, deep=deep + 1,
                       decorate=decorate)
            elif line_sign:
                count += 1
                print(count, sep, str(a000), sep='')
            elif decorate:
                if a000 == value[-1]:
                    print('├ ' * (deeps - 1) + '└ ', a000, sep='')
                else:
                    print('├ ' * deeps, a000, sep='')
            else:
                print(a000)
    else:
        exit(ValueError)
    del cache_count
