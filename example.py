from module1 import *


def test():
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
        convertSystem(b, cm1='money=', returns=False, precision=0.1)
        print(b, '的质因数：', decomposition(b))
        print('转换124181412：')
        convertSystem(124181412, cm1='money=', returns=False, precision=0.1)
        b = filter_(input('输入一个字符串:'), input('将str转换成:'))
        print('转换后:', b)
        print('加密后：', absoluteEncryption((input('输入你要加密的字符串:'))))
        wait(1)
        review(mmm, sep='.', line_sign=1)
        lists_ = list(range(3, 15, 2))
        print('打乱顺序前:', bl(lists_), sep='')
        lists2_ = createRandomList(values=lists_)
        print('打乱顺序后:', review(lists2_), sep='')
        # draw1(right_=False, max_=200, clear_=True)
        get_files('..', True)
        receive('金币')
        createToplevel(title_='advisement', text_='F4F!', xu_hua=0.9, top_most=1)
        breakpoint_(values=1, exit_=False, comment='Press Enter to continue:')
        bomb2(3)
        divisionAlgorithm(42897, 18644)
        bl(aa, all_values=True)
        review(aa)
        print(get_false_unix_time())
        breakpoint_(5, func=lambda: print('程序正常退出（Process finished with exit code 5）'), comment='请按Enter键继续……')
    else:
        print('This is a local function.\n                     ————8388688')


if __name__ == '__main__':
    # ([1, 2, 3, 2, 520, 5, 5, 5, ], 2)
    print(searchToStrInList(['1', ['225', ], '32222222', '232', '225', '5', '22', '2'], '22'))
    test()
