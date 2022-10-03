import math

from module1.data_base import NULL, null, science_tuple
from module1.data_handle import filter_

__all__ = ['average_', 'convertSystem', 'd', 'decomposition',
           'divisionAlgorithm', 'EuclideanAlgorithm', 'R_to_10_convert']


def average_(*args):
    count1 = null
    l1 = []
    sum1 = null
    for a000 in args:
        l1.append(filter_(a000, ('f_dec', 'int',)))
    for a000 in l1:
        count1 += 1
        c = sum1
        sum1 = (c * count1 - c + a000) / count1
        yield sum1
        del c


def convertSystem(value1, cm1='', cm2='', cm3='', returns=False, error_tips_='你输入的数字太大了！', precision=NULL):
    """转换系统

    将一个数以 KM…… 的形式输出

    :param value1: 输入的大数
    :param cm1: 文本1
    :param cm2: 文本2
    :param cm3: 文本3
    :param returns: 默认为False，True时直接忽略cm1, cm2, cm3三个参数，True时返回转换后的值和原来的值，不打印结果，False时只返回转换后的值，打印结果。
    :param error_tips_: 错误提示
    :param precision: 输出精度，例：10表示精确到十位，0.01表示精确到百分位，默认为NULL，（NULL表示无损输出）
    :return: 转换后的数（以str的形式输出）
    """
    re_obj = obj = value1
    count = 0
    pre = 0
    if precision is not NULL:
        pre = 1 / precision
    while (obj >= 1000 or obj <= -1000) and obj != 0 and obj != 1:
        if 1000 > obj > -1000:
            break
        elif obj > 1e66 or obj < -1e66:
            print(error_tips_)
            break
        obj /= 1000
        count += 1
    if obj != 0:
        if obj // 1 == re_obj:
            if precision is not NULL:
                obj = obj * pre // 1 / pre
            if not returns:
                print(cm1, '=', obj, science_tuple[count], sep='')
        else:
            if precision is not NULL:
                obj = obj * pre // 1 / pre
            if not returns:
                print(cm3, '\n', cm1, obj, science_tuple[count], cm2, '\n', sep='')
    if returns:
        return str(obj) + science_tuple[count], re_obj
    else:
        return str(obj) + science_tuple[count]


def d(n=NULL):
    key_ = True
    if n is NULL:
        n = filter_(input('>>>'), 'int')
    else:
        n = filter_(n, 'int')
    for a000 in range(2, math.ceil(math.sqrt(n)), 1):
        if n % a000 == 0:
            key_ = False
            break
    return key_


def decomposition(int1=NULL, tip1='输入一个整数', record=True, safelock=False, errortips='你输入的数字太大了!'):
    """分解质因数

    :param int1: 当 int1 为 NULL 的时候，弹出 tip1 提示输入
    :param tip1: 输入提示，（当 int1 不为 NULL 的时候直接忽略此参数）
    :param record: 是否将此次分解记录，默认为 True
    :param safelock: 安全锁，如果输入的数字 > 1×10⁷ 时退出程序
    :param errortips: 错误提示，只有当启用 safelock 的时候此参数才有效
    :return: 以元组的格式返回分解后的质因数
    """

    obj_list = []
    exclude1 = []
    c2 = 0
    count = r_digit = 1
    if int1 is NULL:
        r_a = a = filter_(input(tip1), 'int')
    else:
        if type(int1) != int:
            r_a = a = filter_(int1, 'int')
        else:
            r_a = a = int1

    while count < math.ceil(math.sqrt(r_a)) and a != 1:  # 重复执行直到 count >= math.sqrt(a) or a == 1
        r_digit += 1
        count += 1
        # print('a=', a, sep='')
        # print('count=', count, sep='')
        # print('ol=', obj_list, sep='')
        # print('len(e1)=', len(exclude1), sep='')
        # print()
        if count in exclude1:
            # print('continue')
            continue
        if a % count == 0:
            a //= count
            obj_list.append(count)
            count = 1
            c2 += 1
            # exclude1.clear()
        if count not in obj_list:
            exclude1.append(count)
        else:
            pass
        if 1 in exclude1:
            while 1 in exclude1:
                exclude1.remove(1)
        if r_digit >= 1e6:
            if safelock:
                print(errortips)
                return 1
        if r_a > 1e7:  # 原 1e11
            print('正在计算第%d个质因数，已完成%2.2f%%' % (c2, (count / (a + 1) * 100)), sep='')
    obj_list.append(a)
    if 1 in obj_list:
        while 1 in obj_list:
            obj_list.remove(1)
    if record:
        file = open('primeNumber.s8l', 'a+')
        for i in obj_list:
            if i not in file:
                file.write(str(i) + ', ')
        file.close()
    if int1 is NULL:
        print(obj_list)
    else:
        return obj_list


def EuclideanAlgorithm(value1, value2, print_=True, p_print=False):
    a = value1
    b = value2
    # count = 0
    # while a != b:
    #     count += 1
    #     if a > b:
    #         a -= b
    #         a = float('%.10f' % a)
    #         b = float('%.10f' % b)
    #         if p_print:
    #             print(count, ')\t', a, '\t', b, sep='')
    #     elif b > a:
    #         b -= a
    #         a = float('%.10f' % a)
    #         b = float('%.10f' % b)
    #         if p_print:
    #             print(count, ')\t', a, '\t', b, sep='')
    #     if count % 100 == 0:
    #         input('请按Enter键继续......')
    # if print_:
    #     print(a)
    # return a

    while a != 0 and b != 0:
        if a > b:
            a %= b
            if p_print:
                print(a, b, sep='\t')
        elif b > a:
            b %= a
            if p_print:
                print(a, b, sep='\t')
        else:
            break
    if a == 0:
        if print_:
            print(b)
        return a
    else:
        if print_:
            print(a)
        return b


def add1(*args):
    """测试版

    :param args:
    :return:
    """
    count = 0

    def add(a, b):
        a1 = filter_(a, 'float')
        b1 = filter_(b, 'float')
        print('a1=', a1, ' b1=', b1, sep='')
        l1 = l2 = NULL
        print(a1, b1)
        if int(a1) == a1 and int(b1) == b1:
            r = int(a1) + int(b1)
        else:
            if '.' in a1:
                l1 = a1.split('.')
            if '.' in b1:
                l2 = b1.split('.')
            r1 = int(l1[0]) + int(l2[0])
            if len(l1[1]) >= len(l2[1]):
                l2[1] += '0' * (len(l1) - len(l2))
            else:
                l1[1] += '0' * (len(l2) - len(l1))
            r2 = int(l1[1]) + int(l2[1])
            r = str(r1) + '.' + str(r2)
        print('r=', r)

        return r

    list1 = list(args)
    for a000 in range(0, len(list1), 1):
        list1[a000] = str(filter_(list1[a000], 'float'))
    for a000 in range(0, len(list1), 2):
        count += add(count, list1[a000])
    return count


def R_to_10_convert(values, r):  # R:无符号十进制整型数
    """进制转换——初步"""
    value_r = filter_(r, ('unsigned', 'f_dec', 'int'))
    output = count = 0
    for a000 in str(values):
        if 58 > ord(a000) >= 48:
            output += int(a000) * value_r ** (len(str(values)) - count)
        elif 65 <= ord(a000) < 91 or 97 <= ord(a000) < 123:
            output += (ord(a000.upper()) - 55) * value_r ** (len(str(values)) - count)
        else:
            print('Invalid values!')
            return -1
        count += 1

    return output / r


divisionAlgorithm = EuclideanAlgorithm
