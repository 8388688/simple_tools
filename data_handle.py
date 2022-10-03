from module1.data_base import NULL

__all__ = ['binarySearch', 'dimensionalList', 'filter_', 'searchToStrInList']


def binarySearch(list2, item):
    low = 0
    high = len(list2) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list2[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return mid
    return None


def dimensionalList(valueList):
    output_list = []
    for a001 in valueList:
        if type(a001) in [list, tuple, set]:
            for a002 in dimensionalList(a001):
                output_list.append(a002)
        else:
            output_list.append(a001)

    return output_list


def filter_(v_str, pattern=('int',), contrary=False, returns=False):
    """字符过滤

    \n 字符过滤，兼容int, oct, dec, bin, hex, float, str, 单个字符, 大写字母, 小写字母, 控制字符等
    \n 字符过滤优先级：
    \n con = control = 1
    \n int = 2
    \n -- 0x = 0o = 0b = 2.1
    \n -- int = 2.2
    \n float = 3
    \n str = 4
    \n -- str_upper = 4.1
    \n -- str_lower = 4.2
    \n -- str_chinese = 4.3
    \n -- str = 4.4
    \n other_signs = 5
    \n -- non_chinese = 5.1
    \n -- non_english = 5.2
    \n other = 5
    \n other = 5
    \n other = 5
    \n other = 5

    \n 也就是说，如果一个 filter_ 同时过滤以下三个进程

    \n  1) filter_('1a213\b1dr4t', 'str_lower')
    \n  2) filter_('1a213\b1dr4t', '1')
    \n  3) filter_('1a213\b1dr4t', 'int')
    \n 那么将会按照 3 - 1 - 2 的顺序执行。
    \n 附：保留字列表：
    \n [int, float, str, str_upper, str_lower, str_chinese, control, con]
    \n [unsigned, no_break, f_dec(强制转换十进制), 'non_chinese', 'non_english']
    \n 有待改进的地方：过滤时忽略 空格、tab和回车

    :param v_str: 必填，过滤的源文件
    :param pattern: 过滤参数
    :param contrary: 反向过滤
    :param returns: 当 returns 为 True 时以元组的形式返回 cache_dict 和 trash，否则只返回 cache_dict
    :return: 当 returns 为 True 时以元组的形式返回 cache_dict 和 trash，否则只返回 cache_dict

    """
    base_string = v_str
    cache_dict = trash = ''
    class_ = pattern
    if 'control' in class_ or 'con' in class_:
        if type(base_string) == int or type(base_string) == float:
            if not contrary:
                cache_dict = ''
            else:
                cache_dict = base_string
        for a000 in base_string:
            if 32 > ord(a000):
                if contrary:
                    trash += a000
                else:
                    cache_dict += a000
            else:
                if contrary:
                    cache_dict += a000
                else:
                    trash += a000
        if cache_dict == '':
            cache_dict = 0.0
        else:
            if not contrary:
                cache_dict = float(cache_dict)
            else:
                cache_dict = str(cache_dict)
    elif 'int' in class_:
        if type(base_string) == int or type(base_string) == float:
            if not contrary:
                cache_dict = int(base_string)
            else:
                cache_dict = 0
        else:
            signs = ('0B', '0O', '0X', '0b', '0o', '0x')
            if base_string[0:2] in signs or 'f_dec' not in class_:
                base_string = str.upper(base_string)
                cache_dict += base_string[0:2]
                if signs.index(base_string[0:2]) == 0 or signs.index(base_string[0:2]) == 3:
                    wall = ('0', '1',)
                elif signs.index(base_string[0:2]) == 1 or signs.index(base_string[0:2]) == 4:
                    wall = ('0', '1', '2', '3', '4', '5', '6', '7',)
                elif signs.index(base_string[0:2]) == 2 or signs.index(base_string[0:2]) == 5:
                    wall = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            'A', 'B', 'C', 'D', 'E', 'F')
                else:
                    wall = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
                for a000 in base_string[2:-1]:
                    if a000 in wall:
                        if contrary:
                            trash += a000
                        else:
                            cache_dict += a000
                    else:
                        if contrary:
                            cache_dict += a000
                        else:
                            trash += a000
                if not contrary:
                    print(cache_dict)
                    if cache_dict in signs:  # 没有什么可转换的
                        cache_dict = 0
                    else:
                        cache_dict = int(eval(cache_dict))
                else:
                    cache_dict = str(cache_dict)
            else:
                for a000 in base_string:
                    if 57 >= ord(a000) >= 48 or (a000 == '-' and cache_dict == '' and 'unsigned' not in class_):
                        if contrary:
                            trash += a000
                        else:
                            cache_dict += a000
                    else:
                        if contrary:
                            cache_dict += a000
                        else:
                            trash += a000
                if cache_dict == '':
                    cache_dict = 0
                else:
                    if not contrary:
                        cache_dict = int(cache_dict)
                    else:
                        cache_dict = str(cache_dict)
    elif 'float' in class_:
        if type(base_string) == int or type(base_string) == float:
            if not contrary:
                cache_dict = float(base_string)
            else:
                cache_dict = 0.0
        else:
            for a000 in base_string:
                if 57 >= ord(a000) >= 48 or '.' not in cache_dict and a000 == '.' or (a000 == '-' and cache_dict == ''):
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
            if cache_dict == '':
                cache_dict = 0.0
            else:
                if not contrary:
                    cache_dict = float(cache_dict)
                else:
                    cache_dict = str(cache_dict)
    elif 'str' in class_ or 'str_upper' in class_ or 'str_lower' in class_:
        if 'str_upper' in class_:
            for a000 in base_string:
                if 90 >= ord(a000) >= 65:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        elif 'str_lower' in class_:
            for a000 in base_string:
                if 121 >= ord(a000) >= 96:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        elif 'str_chinese' in class_:
            for a000 in base_string:
                if 40870 >= ord(a000) >= 13311:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        else:  # elif class_ == 'str':
            for a000 in base_string:
                if 121 >= ord(a000) >= 96 or 90 >= ord(a000) >= 65:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        cache_dict = str(cache_dict)
    elif 'other_signs' in class_:
        if 'non_chinese' in class_:
            # 只过滤英文字符
            wall = ('\"', '\'', '`', '(', ')', '<', '>', '(', ')', '[',
                    ']', '{', '}', ',', '.', '?', '!', ':', ';', '~',
                    '&', '@', '#', '/', '|', '\\', '_', '^',)
        elif 'non_english' in class_:
            # 只过滤中文字符
            wall = ('·', '¨', '´', '«', '»', '¯', '¦', '¡', '¿', '‘',
                    '’', '〝', '〞', '＂', '＇', '【', '】', '《', '》', '＜',
                    '＞', '﹝', '﹞', '〔', '〕', '〈', '〉', '［', '］', '「',
                    '」', '｛', '｝', '〖', '〗', '『', '』', '、', '～', '＆',
                    '＠', '＃', '，', '。', '？', '！', '：', '；', '…', '　',
                    '︵', '︶', '︷', '︸', '︹', '︺', '︿', '﹀', '︽', '︾',
                    '﹁', '﹂', '﹃', '﹄', '︻', '︼', '／', '｜', '＼', '＿',
                    '￣', '﹏', '﹋', '﹍', '﹉', '﹎', '﹊', 'ˋ', '︴', 'ˇ',
                    '¨', 'ˊ', '‹', '›', '︗', '︘',)
            for i in wall:
                print(i + '\', \'' if 127 < ord(i) else '', end='')
        else:
            # 不分全/半角(不分中英，全部过滤)
            wall = ('\"', '‘', '’', '〝', '〞', '\'', '＂', '＇', '`', '(',
                    ')', '【', '】', '《', '》', '＜', '＞', '﹝', '﹞', '<',
                    '>', '(', ')', '[', ']', '〔', '〕', '〈', '〉', '{',
                    '}', '［', '］', '「', '」', '｛', '｝', '〖', '〗', '『',
                    '』', ',', '.', '?', '!', ':', ';', '、', '～', '＆',
                    '＠', '＃', '，', '。', '？', '！', '：', '；', '·', '…',
                    '~', '&', '@', '#', '︵', '︶', '︷', '︸', '︹', '︺',
                    '︿', '﹀', '︽', '︾', '﹁', '﹂', '﹃', '﹄', '︻', '︼',
                    '/', '／', '|', '｜', '\\', '＼', '_', '＿', '￣', '﹏',
                    '﹋', '﹍', '﹉', '﹎', '﹊', 'ˋ', '︴', '^', 'ˇ', '¨',
                    'ˊ', '　', '‹', '›', '︗', '︘', '¨', '´', '«', '¿',
                    '»', '¯', '¦', '¡',)
            for i in wall:
                print(i + '\', \'' if 127 < ord(i) else '', end='')
        for a000 in base_string:
            if a000 in wall:
                if contrary:
                    trash += a000
                else:
                    cache_dict += a000
            else:
                if contrary:
                    cache_dict += a000
                else:
                    trash += a000
        cache_dict = str(cache_dict)
    else:
        length_ = len(class_[0])
        list2 = []
        obj_cache_list = []
        for a001 in base_string:
            list2.append(a001)
            # 把a转换成list的格式存入list2
        for a000 in range(len(list2)):  # a000 是 range（）
            if list2[a000: a000 + length_] == list(class_[0]):
                obj_cache_list.append([a000, a000 + length_])
        obj_cache_list.reverse()
        for a002 in obj_cache_list:
            del [list2[a002[0]: a002[1]]]
        for a000 in list2:
            cache_dict += a000
    if returns:
        return cache_dict, trash
    else:
        return cache_dict


def searchToStrInList(testlist=NULL, input_object=NULL, list_tips='输入一个列表：', obj_tips='输入一个str'):
    output_list = []
    cache_output_list = []
    if testlist is NULL:
        testlist = eval(input(list_tips))
    if input_object is NULL:
        obj2 = input(obj_tips)
    else:
        obj2 = input_object
    # testlist 可以是(), {} 等
    # 因为 OPL(output_list)只是读取 testlist 的内容
    # 并且在读取完后要对 OPL 进行 resort
    for a000 in testlist:
        if (type(obj2) in [str, list, set, dict] and obj2 in a000) or obj2 == a000:
            cache_output_list.append(a000)
    length1 = len(cache_output_list)
    for a000 in cache_output_list:
        if type(obj2) in [str, list, set, dict]:
            if a000 == obj2:
                output_list.append([-1, a000])
            else:
                for a001 in range(0, len(a000), 1):
                    if a000[a001: a001 + len(obj2)] == obj2:
                        output_list.append([a001, a000])
                        break
        else:
            output_list.append([-1, a000])
    del cache_output_list[::]
    # ->
    cache_output_list = sorted(output_list,
                               key=lambda x: x[0])
    # cache_output_list 此时应该是 list 的形式，如果是 str 的话，就在 "->" 记号处插入一个 eval()
    del output_list[::]
    for a000 in range(len(cache_output_list)):
        output_list.append(cache_output_list[a000][1])
    print('搜索结果：', output_list)
    del output_list, cache_output_list, length1
