import os
import sys
from typing import Callable

# from simple_tools.system_extend import delete

__all__ = ["deprecated", "invoke", "is_exec", "check_and_install_package"]
__version__ = "4.8-beta1"
version_code = 20250722001


def deprecated(fx: str | Callable, recommend=None) -> str:
    context = (f"{fx if isinstance(fx, str) else fx.__name__} 已弃用"
               f"{f'，推荐使用 {recommend.__name__}' if recommend is not None else ''}")
    print(context)
    return context


def invoke(fx: str | Callable, fx_api):
    context = f"{fx if isinstance(fx, str) else fx.__name__} 调用的是 {fx_api.__name__} 的 API"
    print(context)
    return context


def get_update():
    import warnings
    warnings.warn(deprecated(get_update),
                  DeprecationWarning, stacklevel=4)
    return 0


def is_exec():
    return hasattr(sys, "_MEIPASS")


def check_and_install_package(*args, import_=False, noWarning=False):
    print(
        '\033[0;31m' + check_and_install_package.__name__ + ' 目前主要问题：无法检测过时升级的包，也无法自动升级这些包。\033[0m')
    with os.popen("\"" + sys.executable + f"\" -m pip freeze", "r") as pipeline:
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
            os.system("\"" + sys.executable + f"\" -m pip install {pkg}")
            print("安装完成，", end="")
        else:
            print(f'You have already installed \"{pkg}\" package.')
        if import_:
            __import__(pkg)
            print(f"导入 {pkg} 库")
        else:
            print(f"执行以下语句以导入 {pkg} 库。\n-> import {pkg}")


if __name__ == '__main__':
    get_update()
