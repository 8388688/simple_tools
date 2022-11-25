from simple_tools import *


def test():
    # from __init__.py
    if __name__ == '__main__':
        human1 = Person('steve')
        user1 = Users()
        user2 = Users('电话')
        u1 = ''
        u2 = ' '
        while not u1:
            u1 = input('输入用户名(ran表示随机)')
            if u1 == 'ran':
                u1 = Users.returnName()
                c = 0
                while u2 != 'y':
                    u2 = input('%s 这个用户名您满意吗？(y/n)' % u1)
                    if u2 == 'n':
                        u1 = Users.returnName()
                        c += 1
                    else:
                        c += 5
                    if c >= 250:
                        print('\033[1;31m你是存心来捣乱的吧！\033[0m')
                        times.sleep(1)
                        exit(0)
                if u2 == 'y':
                    break
        user3 = Users(u1)
        print(user1, user2, user3, human1, sep='\n')
        mmm = {'金币': 0, '银币': 5, '铜板': 15}
        aa = ['f', 'u', [['n', 'c'], 't', ['i', 'o', 'n']]]
        b = filter_(input('输入一个大于300的数:'), ('f_dec', 'int'))
        while b <= 300:
            b = filter_(input('输入一个大于300的数:'), ('f_dec', 'int'))
        convert_system(b, cm1='money=', returns=False, precision=0.1)
        print(b, '的质因数：', decomposition(b))
        print('转换124181412：')
        convert_system(124181412, cm1='money=', returns=False, precision=0.1)
        b = filter_(input('输入一个字符串:'), input('将str转换成:'))
        print('转换后:', b)
        print('加密后：', absolute_encryption((input('输入你要加密的字符串:'))))
        wait(1)
        review(mmm, sep='.', line_sign=1)
        lists_ = list(range(3, 15, 2))
        print('打乱顺序前:', bl(lists_), sep='')
        lists2_ = create_random_list(values=lists_)
        print('打乱顺序后:', review(lists2_), sep='')
        # draw1(right_=False, max_=200, clear_=True)
        get_files('..', True)
        receive('金币')
        create_toplevel(title_='advisement', text_='F4F!', xu_hua=0.9, top_most=1)
        breakpoint_(values=1, exit_=False, comment='Press Enter to continue:')
        bomb2(3)
        divisionAlgorithm(42897, 18644)
        bl(aa, all_values=True)
        review(aa)
        print(get_time_stamp())
        breakpoint_(5, func=lambda: print('程序正常退出（Process finished with exit code 5）'),
                    comment='请按Enter键继续……')
    else:
        print('This is a local function.\n                     ————8388688')


def system_of_test():
    # from system_extend.py
    for k in generate_file_path(r'C:\Users\taskmgr_agent\AppData\Local\Application Data', True, from_size=1000,
                                to_size=1000000, suffix='exe'):
        print(k)


def get_suffix():
    # from default.py
    fp_1 = '..\\'
    k = set()
    for i in generate_file_path(fp_1, False):
        try:
            k.update({i.split('.')[-1]})
        except:
            print(k)
        finally:
            print(i)
    k = sorted(list(k))
    print(k)


def bl_properties():
    # from data_process.py
    seq = [0, [[1, 2, (3, [4, 5, 6, {7.1: 'a', 7.2: 'b'}],), [8, {}, [9, (10, 11), 12], ], [], ], 13, {14, 15, }, 16],
           17, 18]
    print(seq)
    for d in generate_bl_properties(seq):
        print(d)
    print('-' * 50)
    bl_properties(seq, True, True)
    print('-' * 50)
    bl_properties({1: 2, 3: 4})
    print('-' * 50)
    bl_properties([[], [[], [[], [[], [[], [[], [[], [[], [[], [[], [[], [[], ['a', ], 'f', ],
                                                                     'f', ], 'f', ], 'f', ],
                                                      'f', ], 'f', ], 'f', ], 'f', ], 'f', ],
                             'f', ], 'f', ], 'f', ],
                  True, True)
    print('-' * 50)


def file_class_test():
    # from system_extend.py
    # file_example = File(r'I:\2020\8388688\病毒隔离区\kw\kw1_2_7.bat')
    file_example = File(r'I:\2020\8388688\病毒隔离区')
    print('文件路径fp=', file_example.fp)
    print('完整路径file_path=', file_example.file_path)
    print('文件名name=', file_example.name)
    print('扩展名(后缀)suffix=', file_example.suffix)
    # print('创建时间ct=', file_example.ct)
    print('转换后的ct=', get_time_stamp(file_example.ct))
    # print('修改时间mt=', file_example.mt)
    print('转换后的mt=', get_time_stamp(file_example.at))
    # print('访问时间at=', file_example.at)
    print('转换后的at=', get_time_stamp(file_example.at))
    print('大小size=', file_example.size)


def normal_encr_test():
    # from encr_decr
    for a004 in range(0, 10, 1):
        s = input('>>>')
        print(s)
        print(get_md5(s))
        print(normal_encryption(s, True, key='1234567', key_length=8, details=True))
        # print(normal_encryption(normal_encryption(s, True), False))

    # e = md5Encryption('I am a string.')
    # print(e)


def user_registry():
    # from game_disposition.py
    user1 = Users(name='6c4f2bbf-30a2-326c-90fe-', mode=0, psd='胡')
    user1.topUp(25)
    user1.save_user_info()


if __name__ == '__main__':
    # ([1, 2, 3, 2, 520, 5, 5, 5, ], 2)
    print(search_to_str_in_list(['1', ['225', '2025'], '32222222', '232', '0225', '5', '22', '2'], '22'))
    system_of_test()
    test()