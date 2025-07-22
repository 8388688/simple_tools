from simple_tools import *


def test():
    # from __init__.py
    print("本函数适配 simple_tools 4.8+")
    if __name__ == '__main__':
        aa = ['f', 'u', [['n', 'c'], 't', [
            'i', 'o', 'n'], {'金币': 0, '银币': 5, '铜板': 15}]]
        b = 0
        while b <= 300:
            b = filter_(input('输入一个大于300的数:'), ('f_dec', 'int'))
        print(b, '的质因数：', decomposition(b))
        print("科学计数法(1000)：", scientific_notate(b))
        print("科学计数法(1024)：",
              scientific_notate(b, rate=1024, custom_seq=("Byte", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB")))
        b = filter_(input('输入一个字符串:'), input('将str转换成:'))
        print('转换后:', b)
        print('等待3秒')
        wait(3)
        lists_ = list(range(3, 15, 2))
        print('打乱顺序前:', lists_)
        wait(1)
        for i in tree_fp_gen(input("输入任意路径："), True, keepend=False):
            print(end=i)

        print(gcd(42897, 18644))
        for i in bl_properties_gen(aa):
            print(i)

    else:
        print('This is a local function.\n%s————8388688' % " " * 20)


def normal_encr1():
    string1 = 'ABC! I am a sorting. ~!@#$%^&*()_+}{\"|?><:,/.\';\\[]-=' \
              '中文语言字符串, 〩~！@#￥%……&……*（）{——+}|“：》《？，。、；’【、-】=ffs___    df'
    bin_test = b'\xb0\xa1\xca\xd6\xb6\xaf\xb7\xa7\xb7\xa2\xc9\xe4\xb5\xe3\xb7\xa2\xc9\xfadads\xb7\xb6\xb5\xc2\xc8\xf8' \
               b'\xb7' \
               b'\xa2\xc9\xfa\xb5\xc4 % file_c % file_c % file_c % file_c % file_c % ' \
               b'file_c\xc8\xcb\xc9\xf9\xb6\xa6\xb7\xd0\xb9\xe3\xb6\xab\xca\xa1\r\n\r\n\r\n\xb5\xab\xca\xc7 ' \
               b'\\b\\nn\\n\\\\bb\\vb\\\\\r\nvvs 23g1ewr164\xa1\xb7\xa1\xb6\xa3\xbf\xa1\xb1|\xa3\xba}{' \
               b'+\xa3\xa9\xa1\xaa\xa1\xaa*\xa3\xa8*\xa1\xad\xa1\xad%\xa1\xad\xa1\xad\xa3\xa4#@\xa3\xa1~1\xa1' \
               b'\xa423299806' \
               b'\xa3\xac\xa1\xa2\xa1\xa3\xa1\xae\xa3\xbb\xa1\xa2\xa1\xbe\xa1\xbf-4=gbhdrehg\r\n\r\n\xb5\xc3\xb5\xbd' \
               b'\r\nf' \
               b'\r\n\r\nc\r\n '
    c = rsa_crypt_easy(bin_test, 2, quiet=False, chunks=1)
    # =========================
    print("原始的:", bin_test)
    print("加密后:", c)
    d = rsa_crypt_easy(c, -2, quiet=False, chunks=1)
    print("解密后:", d)
    print("相等?", bin_test == d)
    print(rsa_crypt([132456489765465464984499, ], 2))


def get_Q_RECOVGERED_FROM_H_suffix():
    import os
    if input("up?:"):
        suf = dict()
        for i in fp_gen(r"Q:\\Recovered_from_h"):
            suf.update({os.path.splitext(
                i)[-1].lower(): suf.get(os.path.splitext(i)[-1].lower(), 0) + 1})
    else:
        suf = {}
    print(suf)
    suf2 = sorted(suf, key=lambda x: suf[x], reverse=True)
    for i in suf2:
        if suf[i] < 20:
            pass
        else:
            print(i, suf[i])


if __name__ == "__main__":
    # test()
    # normal_encr1()
    test()
