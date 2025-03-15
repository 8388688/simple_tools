from simple_tools import *


def test():
    # from __init__.py
    if __name__ == '__main__':
        print(timestamp(presets=3))
        human1 = Person('steve')
        user1 = Users() if random_choice_old() else Users('电话')
        u1 = ''
        u2 = ' '
        while not u1:
            u1 = input('输入用户名(ran表示随机)')
            if u1 == 'ran':
                u1 = Users.returnName(user1)
                c = 0
                while u2 != 'y':
                    u2 = input('%s 这个用户名您满意吗？(y/n)' % u1)
                    if u2 == 'n':
                        u1 = Users.returnName(user1)
                        c += 5
                    else:
                        c += 1
                    if c >= 250:
                        print('\033[1;31m你是存心来捣乱的吧！\033[0m')
                        times.sleep(1)
                        exit(0)
                if u2 == 'y':
                    break
        user3 = Users(u1)
        print(user1, user3, human1, sep='\n')
        aa = ['f', 'u', [['n', 'c'], 't', ['i', 'o', 'n'], {'金币': 0, '银币': 5, '铜板': 15}]]
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
        lists2_ = create_random_list(values=lists_)
        print('打乱顺序后:', lists2_)
        wait(1)
        for i in tree_fp_gen('../simple_tools', 1):
            print(i)

        print(gcd(42897, 18644))
        for i in bl_properties_gen(aa):
            print(i)

    else:
        print('This is a local function.\n%s————8388688' % " " * 20)


def file_class_test():
    # from system_extend.py
    # file_example = File(r'I:\2020\8388688\病毒隔离区\kw\kw1_2_7.bat')
    file_example = File(r'I:\2020\8388688\病毒隔离区')
    print('文件路径fp=', file_example.fp)
    print('完整路径file_path=', file_example.file_path)
    print('文件名name=', file_example.name)
    print('扩展名(后缀)suffix=', file_example.suffix)
    # print('创建时间ct=', file_example.ct)
    print('转换后的ct=', timestamp(file_example.ct))
    # print('修改时间mt=', file_example.mt)
    print('转换后的mt=', timestamp(file_example.at))
    # print('访问时间at=', file_example.at)
    print('转换后的at=', timestamp(file_example.at))
    print('大小size=', file_example.size)


def user_registry():
    # from game_disposition.py
    user1 = Users(name='6c4f2bbf-30a2-326c-90fe-', mode=0, psd='胡')
    user1.topUp(25)
    user1.save_user_info()


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


if __name__ == "__main__":
    # test()
    # normal_encr1()
    import os

    if input("up?:"):
        suf = dict()
        for i in fp_gen(r"Q:\\Recovered_from_h"):
            suf.update({os.path.splitext(i)[-1].lower(): suf.get(os.path.splitext(i)[-1].lower(), 0) + 1})
    else:
        suf = {'.txt': 426, '.mp4': 107, '': 1835, '.metadata-v2': 3, '.swp': 1, '.html': 1336, '.log': 272, '.jpg': 32,
               '.cache-8': 13, '.myb': 354, '.ott': 77, '.gif': 20, '.svg': 6396, '.sqlite': 36, '.sqlite-shm': 29,
               '.bat': 51, '.db': 36, '.png': 1551, '.sav': 2, '.tex': 1, '.md': 270, '.js': 93, '.jpeg': 1, '.url': 10,
               '.css': 67, '.jsonp': 1, '.db-wal': 3, '.db-shm': 4, '.wxapkg': 1, '.docx': 7, '.m4a': 2, '.dbc': 1,
               '.xml': 1007, '.batch': 3, '.dict': 3, '.knowledge': 1, '.regex': 1, '.bmp': 16, '.jsp': 59, '.xye': 15,
               '.zip': 36, '.py': 4979, '.profile': 7, '.tcl': 172, '.php': 1621, '.java': 76, '.kmm': 27,
               '.properties': 630, '.twig': 270, '.kml': 61, '.json': 179, '.lz4': 6, '.xsl': 66, '.pfs': 62,
               '.strings': 148, '.msg': 146, '.nlf': 136, '.nsh': 351, '.sh': 29, '.pem': 48, '.hash': 2, '.nsi': 178,
               '.wav': 43, '.sample': 18, '.rst': 4, '.ffs_gui': 54, '.pack': 123, '.sdg': 11, '.sdv': 14, '.str': 9,
               '.thm': 14, '.ps': 33, '.a': 20, '.au': 12, '.inf': 2, '.ix': 2, '.fmt': 2, '.bashrc': 1,
               '.bash_logout': 1, '.jspx': 2, '.otp': 23, '.dbf': 2, '.dbt': 2, '.odb': 4, '.ots': 18, '.certs': 1,
               '.map': 9, '.scss': 82, '.otg': 1, '.bsh': 17, '.crt': 10, '.tag': 4, '.pdf': 21, '.rar': 2,
               '.policy': 3, '.pc': 1, '.exe': 11, '.mod': 14, '.manifest': 17, '.pf': 5, '.ods': 7, '.info': 3,
               '.me': 2, '.ico': 4, '.jspf': 2, '.inc': 3, '.rdb': 12, '.def': 10, '.c': 8, '.in': 3, '.cpp': 2,
               '.dsp': 6, '.pyi': 14, '.adobe': 1, '.gpl2': 1, '.gplv2': 2, '.gplv3': 1, '.lesser': 2, '.lib': 13,
               '.runtime': 1, '.bau': 12, '.sql': 4, '.fodt': 1, '.dist': 4, '.data': 1, '.p': 2, '.ldif': 1, '.ini': 5,
               '.mo': 11, '.po': 50, '.bin': 16, '.tld': 3, '.env': 4, '.interp': 4, '.jfc': 2, '.otr': 1, '.ttf': 12,
               '.z': 4, '.list': 1, '.chm': 9, '.reg': 25, '.gpg': 1, '.stw': 2, '.7z': 2, '.asp': 6, '.xye~': 2,
               '.vbs': 2, '.dic': 16, '.spl': 3, '.sug': 3, '.sing': 7, '.sln': 3, '.vcproj': 2, '.dpr': 5, '.pmap': 1,
               '.voucher': 2, '.bfc': 1, '.src': 1, '.xpi': 3, '.pdb': 1, '.chk': 3, '.bash': 1, '.tcsh': 1, '.zsh': 1,
               '.its': 5, '.pickle': 4, '.uue': 8, '.desktop': 2, '.key_': 237, '.tree': 238, '.tm': 6, '.lgr': 4,
               '.icns': 2, '.pyw': 2, '.odt': 1, '.rc': 2, '.lock': 1, '.xsd': 3, '.security': 1, '.cpl': 1,
               '.access': 1, '.template': 4, '.xpt': 2, '.qm': 190, '.xyr': 1, '.oxygen': 1, '.putty': 3, '.rtf': 1,
               '.terms': 1, '.lua': 8, '.cache': 2, '.alias': 1, '.rdf': 9, '.old': 11, '.eps': 2, '.llc': 8, '.mgc': 1,
               '.wsf': 2, '.78': 1, '.types': 1, '.pot': 2, '.xsb': 1, '.t1': 26, '.pas': 2, '.ja': 5, '.woff': 6,
               '.module': 1, '.devhelp2': 1, '.pat': 2, '.doc': 3, '.fish': 1, '.htm': 30, '.whl': 4, '.example': 1,
               '.aiff': 8, '.aifc': 2, '.pref': 4, '.hhc': 2, '.hhp': 2, '.ncx': 1, '.opf': 1, '.orig': 6, '.hlp': 2,
               '.pth': 2, '.o': 2, '.pbm': 2, '.pgm': 2, '.ppm': 3, '.ras': 2, '.sgi': 2, '.tiff': 2, '.iml': 3,
               '.pck': 6, '.abw': 2, '.portable': 1, '.xulrunner': 1, '.i386': 1, '.crl': 2, '.exception': 1, '.war': 1,
               '.eterm': 4, '.gnome': 4, '.konsole': 4, '.linux': 4, '.mrxvt': 4, '.rxvt': 4, '.xterm-new': 4,
               '.konsole-256color': 2, '.linux-m1': 2, '.linux-m1b': 2, '.linux-m2': 2, '.minitel1': 2,
               '.minitel1-nb': 2, '.minitel12-80': 2, '.minitel1b': 2, '.minitel1b-80': 2, '.minitel1b-nb': 2,
               '.minitel2-80': 2, '.mlterm': 2, '.mlterm-256color': 2, '.putty-256color': 2, '.putty-m1': 2,
               '.putty-m1b': 2, '.putty-m2': 2, '.teraterm': 2, '.vte': 2, '.vte-256color': 2, '.xterm-256color': 2,
               '.xterm-r6': 2, '.xterm-xfree86': 2, '.msi': 2, '.tmpl': 4, '.mozlz4': 1, '.fdb': 1, '.vcxproj': 1,
               '.filters': 1, '.mes': 1, '.xaml': 7, '.aif': 2, '.com': 2, '.cmd': 6, '.little': 4, '.sqlite-wal': 1,
               '.hrc': 1, '.pid': 3, '.profile-am-et': 2, '.profile-ar': 2, '.profile-ar-eg': 2, '.profile-ar-sa': 2,
               '.profile-bg-bg': 2, '.profile-ca-es': 2, '.profile-cp1254': 2, '.profile-cs-cz': 2, '.profile-da-dk': 2,
               '.profile-de': 2, '.profile-de-at': 2, '.profile-de-ch': 2, '.profile-de-de': 2, '.profile-div-mv': 2,
               '.profile-el-gr': 2, '.profile-en': 2, '.profile-en-au': 2, '.profile-en-ca': 2, '.profile-en-gb': 2,
               '.profile-en-ie': 2, '.profile-en-nz': 2, '.profile-en-us': 2, '.profile-en-za': 2, '.profile-es': 2,
               '.profile-es-es': 2, '.profile-es-mx': 2, '.profile-eu': 2, '.profile-eu-es': 2, '.profile-fa-ir': 2,
               '.profile-fi-fi': 2, '.profile-fr': 2, '.profile-fr-be': 2, '.profile-fr-ca': 2, '.profile-fr-ch': 2,
               '.profile-fr-fr': 2, '.profile-gl-es': 2, '.profile-he': 2, '.profile-he-il': 2, '.profile-hu-hu': 2,
               '.profile-it-it': 2, '.profile-ja-jp': 2, '.profile-kk-kz': 1, '.profile-koi8-r': 2,
               '.profile-koi8-u': 2, '.profile-koi8-ub': 2, '.profile-lt-lt': 2, '.profile-nb-no': 2,
               '.profile-nl-nl': 2, '.profile-nn-no': 2, '.profile-pl-pl': 2, '.profile-ps': 2, '.profile-pt-br': 2,
               '.profile-pt-pt': 2, '.profile-ro': 2, '.profile-ro-ro': 2, '.profile-ru': 2, '.profile-ru-ru': 2,
               '.profile-sk-sk': 2, '.profile-sl': 2, '.profile-sv': 2, '.profile-sv-se': 2, '.profile-syr': 2,
               '.profile-tr': 2, '.profile-tr-tr': 2, '.profile-uk-ua': 2, '.profile-ur-pk': 2, '.profile-yi': 2,
               '.profile-zh-cn': 2, '.profile-zh-tw': 2, '.out': 2, '.tar': 2, '.tri': 2, '.vbox-prev': 2, '.avi': 2,
               '.idx': 1, '.bar': 1, '.utf-8': 32, '.ca': 1, '.de': 1, '.eo': 1, '.es': 1, '.fr': 1, '.hr': 1, '.hu': 1,
               '.it': 1, '.euc': 3, '.sjis': 1, '.ko': 1, '.nb': 1, '.nl': 1, '.no': 1, '.pt': 1, '.ru': 1, '.sk': 1,
               '.sv': 1, '.iso9': 1, '.big5': 1, '.img': 3, '.viso': 3, '.bak': 2, '.mdmp': 1, '.tmp': 2, '.webm': 1,
               '.vbox': 1, '.s': 1, '.biolg': 2, '.x': 1, '.t': 1, '.y': 1, '.wim': 1, '.key': 1, '.vdi': 1,
               '.kdbx': 37}
    print(suf)
    suf2 = sorted(suf, key=lambda x: suf[x], reverse=True)
    for i in suf2:
        if suf[i] < 20:
            pass
        else:
            print(i, suf[i])
