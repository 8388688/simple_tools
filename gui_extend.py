# 以后可能会加进更多东西（可能得等到 2026 年以后，目前不要抱太大希望）。

import os
from sys import executable


__all__ = ['check_and_install_package']


def check_and_install_package(*args, import_=False, noWarning=False):
    print(
        '\033[0;31m' + check_and_install_package.__name__ + ' 目前主要问题：无法检测过时升级的包，也无法自动升级这些包。\033[0m')
    with os.popen("\"" + executable + f"\" -m pip freeze", "r") as pipeline:
        pkg_list = [x.strip('\n').split('==')[0] for x in pipeline.readlines()]

    for pkg in args:
        '''
        try:
            import "pkg"
        except ModuleNotFoundError:
            print(f"\n您没有安装 {pkg} 库，正在为您自动安装！")
            system("\"" + executable + f"\" -m pip install {pkg}")
            print("安装完成！")
            import "pkg"
        '''
        if pkg not in pkg_list:
            print(f"\n您没有安装 {pkg} 库，正在为您自动安装。")
            os.system("\"" + executable + f"\" -m pip install {pkg}")
            print("安装完成，", end="")
        else:
            print(f'You have already installed \"{pkg}\" package.')
        if import_:
            __import__(pkg)
            if not noWarning:
                print(
                    "\033[0;31m由于 exec() 命令自身的漏洞，启用自动导入安装的模块选项有一定的危险性，勿滥用 exec() 命令。\033[0m;")
                print("\033[0;31m隐藏这行提示请使用 noWarning=True 参数\033[0m;")
            else:
                print(f"导入 {pkg} 库")
        else:
            print(f"执行以下语句以导入 {pkg} 库。\n-> import {pkg}")
