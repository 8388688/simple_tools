# 素材大本营
# 版本 V2.4.4
# 最后修改时间：20220312175940
#
# 1.6.6 以前的版本全部损坏，无法读取。
# All versions of module1 before 1.6.6 are broken and can't be read.
# 2.0.1 以前的版本创建、修改和访问时间间隔太长，损坏严重，无法读取。
# Version 2.0.1 before create, modify,
# and access time interval is too long,
# was badly damaged and can't read
# ---------- 20200320 ----------
# 2.4.4 更改: 1.创建 example.py 文件
#             2.
# ---------- 20200312 ----------
# 2.4.3 更改: 1.修正 get_file_path_of_generator 无法返回所有文件夹的 bug
#             2.更新 file_remove, get_file_name, file_pattern
# ---------- 20200305 ----------
# 2.4.2 更改: 添加 random_choice 函数
# 2.4.1 更改: 1.删除 create_random 变量
#             2.更新 file_pattern 函数, 添加 easy_options 参数
# 2.4   更改: 1.创建 times.py 文件
#             2.在 times.py 中创建 get_false_unix_time 函数
#             3.移动 wait 函数到 times.py 中
#             4.更新 __init__.py 的 __all__ 变量
# ---------- 20200226 ----------
# 2.3.1   更改: 1.创建 hash_values.py 文件
#             2.把 get_md5 函数移到 hash_values.py 下
# 2.3   更改: 1.更新并完善 filter_ 的 other_signs 参数
#             2.在 data_base.py 中加入 tabs 元组
#             3.更新 __all__ 变量
# ---------- 20200219 ----------
# 2.2.3 更改: 1.更新 filter_ 的 other_signs 参数
#             2.删除 test() 中的 draw1 引用
# 2.2.2 更改: 加入 binarySearch 函数
# ---------- 20220205 ----------
# 2.2.1 更改: rename username to usernameList
# 2.2   更改: 1.rename str_handle to data_handle
#             2.删除 default 中的 createToplevel
#             3.创建 test.py
# ---------- 20220203 ----------
# 2.1   更改: 1.更新 file_remove 函数无法删除文件夹的 bug,
#             2.增加 file_pattern 函数.
#             3.在 system_.py 中添加 fp = getcwd() 常量
#             4. 创建 dimensionalList 在 data_handle.py
# 2.0.1 更改: 修正模块常量无法导入的问题
# -----------  更早  -----------
# 2.0   更改: 1.创建 file_remove, 大规模升级 system_.py,
#             2.修正 get_file_path_of_generator 的 bug,
#             3.加入常量 EOF = -1, NULL = None, null = 0,
#             4.删除 __init__.py 的 absoluteEncryption,
#             5.创建 data_base.py 数据库.
#
# 1.8   更改: 创建 system_.py, 移动 get_file_name, get_file_name_of_generator,
#             get_file_path, get_file_path_of_generator, get_file_size,
#             get_files, get_file_names 到 system_.py
#
# 1.7.1 更改: 1.更新 Users,
#             2.pw 用 md5 加密.
# 1.7   更改: 1.删除 __init__.py 的 review, digitalDecryption, draw1, draw2, breakpoint_,
#             2.修正 breakpoint_ 中 exit_ 的 bug,
#             3.创建 randoms.py 并添加 createRandomList,
#             4.删除 __init__.py 的 passed, EuclideanAlgorithm.
#
# 1.6.13 更改: 修正 get_file_path 的 bug.
# 1.6.12 更改: 给 get_file_name 添加注释.
# 1.6.11 更改: 1.更新 username 词库,
#              2.修改随机起名的 bug.
# 1.6.10 更改: 1.更新 filter_ R 进制过滤的 bug,
#              2.把 get_files 改名为 get_file_path.
# 1.6.9 更改: 1.更新 EuclideanAlgorithm,
#             2.删除 __init__.py 的 bl.
# 1.6.8 更改: 1.把 divisionAlgorithm 函数更名为 EuclideanAlgorithm,
#             2.删除 __init__.py 的 conversionSystem.
# 1.6.7 更改: 加进 get_file_name 和 get_files 两个函数在 default.py 中.

###################################################################################

import tkinter.simpledialog
from hashlib import md5
from time import *

from module1.data_base import *

from module1.bomb import *
from module1.data_handle import *
from module1.default import *
from module1.draws import *
from module1.encryption import *
from module1.hash_values import *
from module1.maths import *
from module1.passed import *
from module1.randoms import *
from module1.review import *
from module1.system_ import *
from module1.times import *

__all__ = ['bomb', 'data_base', 'data_handle', 'default', 'draws', 'encryption',
           'maths', 'passed', 'randoms', 'review', 'system_', 'times',

           'delete', 'EOF', 'fp', 'NULL', 'null', 'cacheTimes', 'money',
           'science_tuple', 'tabs', 'usernameList',

           'Person', 'Users',

           'absoluteEncryption', 'average_', 'binarySearch',
           'bl', 'bomb1', 'bomb2', 'breakpoint_', 'convertSystem',
           'createToplevel', 'createRandomList', 'd', 'decomposition',
           'digitalDecryption', 'dimensionalList',
           'draw1', 'draw2', 'EuclideanAlgorithm',
           'fileEncryption', 'file_pattern', 'file_remove',
           'filter_', 'get_false_unix_time', 'get_file_name',
           'get_file_name_of_generator', 'get_file_path',
           'get_file_path_of_generator', 'get_file_size',
           'get_file_suffix', 'get_md5', 'normalEncryption',
           'pass_', 'R_to_10_convert', 'random_choice', 'random_pop',
           'receive', 'review', 'searchToStrInList', 'wait',

           'delete', 'divisionAlgorithm',
           'get_files', 'get_file_names', ]


class Person:
    def __init__(self, name):
        self.name = name
        self.life = 100
        self.hunger = 0
        self.experience = 0
        self.physicalStrength = 30
        self.defense = 30
        self.foods = {'food': {'土豆': 5, '面包': 3, '胡萝卜': 3, '牛奶': 3},
                      'fruits': {'苹果': 2, '香蕉': 2, '葡萄': 2, '梨': 2, '菠萝': 2},
                      'meats': {'生羊肉': 5, '生猪肉': 5, '生牛肉': 3, '生鱼': 3}}

    def __str__(self):
        return self.name + '的资料：\n生命值:' + str(self.life) + '\n饥饿值:' + str(self.hunger) \
               + '\n经验值' + str(self.experience) + '\n体力:' + str(self.physicalStrength) \
               + '\n防御值' + str(self.defense)

    def __del__(self):
        del self.life, self.hunger, self.experience, self.physicalStrength, self.defense, self.foods
        print(self.name, '已死亡')
        del self.name


class Users:
    UserNameList = []

    def __init__(self, name=NULL, psd='', encoding='UTF-8'):
        if name is NULL:
            name = usernameList[0][random.randint(0, len(usernameList[0]))] + '的' + usernameList[3][
                random.randint(0, len(usernameList[3]))] + usernameList[1][random.randint(0, len(usernameList[1]))]
        if name not in Users.UserNameList:
            self.name = name
            self.state = 0  # 0=正常离线 1=在线 -1=不允许上线
            self.password = md5(psd.encode(encoding=encoding)).hexdigest()
            # self.password = psd
            self.money = 500
            self.diamonds = 60
            Users.UserNameList.append(self.name)
        else:
            print(name, '这个用户名已存在！')
            del self

    def __str__(self):
        return '当前用户：' + str(self.name)

    def __del__(self):
        print('正在注销', self.name, '用户的登录...')
        del self.state, self.password, self.money, self.diamonds
        print('已注销', self.name, '用户的登录...')
        del self.name

    def topUp(self):
        self.money += 10
        self.diamonds -= 1
        print('充值10金币')

    def returnName(self):
        """返回一个随机名字

        返回一个随机名字，与User配对使用
        """
        u = usernameList[0][random.randint(0, len(usernameList[0]) - 1)] + '的' + usernameList[3][
            random.randint(0, len(usernameList[3]) - 1)] + usernameList[1][random.randint(0, len(usernameList[1]) - 1)]
        while u in Users.UserNameList:
            u = usernameList[0][random.randint(0, len(usernameList[0]) - 1)] + '的' + usernameList[3][
                random.randint(0, len(usernameList[3]) - 1)] + usernameList[1][
                    random.randint(0, len(usernameList[1]) - 1)]
        return u

    def login(self, name, password=NULL):
        pass

    def register(self):
        pass
