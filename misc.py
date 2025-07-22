import sys
from typing import Callable
from http.client import RemoteDisconnected
from os.path import join
from traceback import format_exc
from webbrowser import open as webbopen  # web browser open

from requests import get
from requests.exceptions import ConnectTimeout, ConnectionError

from simple_tools.data_base import ST_WORK_SPACE
# from simple_tools.system_extend import delete

__all__ = ["deprecated", "invoke", "is_exec"]
__version__ = "4.7 Release"
version_code = 20250722001

LOG_FILE_PATH = join(ST_WORK_SPACE, 'default', 'get_update.txt', )
log_file_entity = open(LOG_FILE_PATH, 'a')
log_file_entity.close()


def clear_module_cache():
    import warnings
    warnings.warn(f"{deprecated(clear_module_cache)}",
                  DeprecationWarning, stacklevel=4)
    print("在清除缓存后，程序会强制退出，以避免缓存缺失带来的问题。")
    print("准备清除缓存。")
    # delete(ST_WORK_SPACE, all_files=True, all_folders=True, forces=True)
    print("Complete!")
    exit(0)


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
                  PendingDeprecationWarning, stacklevel=4)

    global log_file_entity
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/107.0.0.0 Safari/537.36',
        # 'Connection': 'close'  # 不使用持久连接
    }
    new_info = get(r'https://raw.githubusercontent.com/8388688/simple_tools-st/main/version.json',
                   headers=headers).json()

    # print(new_info, type(new_info))
    if new_info['updatecontent'][new_info['version']][0] > version_code:
        print('有新版本可用：', new_info['version'], '（当前版本', __version__, '），更新内容：')
        for v in new_info['updatecontent']:  # 输出更新内容
            if new_info['updatecontent'][v][0] <= version_code:
                break
            print('└- ' + v + '：' + new_info['updatecontent'][v][1])
        if input('自动更新？（y/n）') == 'y':
            try:
                # 这里需要对 url 更新
                req = get(new_info['updatecontent']
                          [new_info['version']][3], stream=True)
            except ConnectionRefusedError:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('[WinError 10061] 似乎 github.com 已拒绝连接。[ConnectionRefusedError]')

            except ConnectTimeout:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('github.com 加载缓慢。[ConnectTimeout]')
            except TimeoutError:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('github.com 连接超时。[TimeoutError]')
            except ConnectionError:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('无法连接 github.com。[ConnectionError]')
            except RemoteDisconnected:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('请求头的 User-Agent 错误。[RemoteDisconnected]')
            else:
                accident_is_happen = False

            if accident_is_happen:
                print('是否打开镜像源（gitee.com）手动更新？(y/n)')
                log_file_entity = open(LOG_FILE_PATH, 'a')
                log_file_entity.write(traceback_exc + '\n')
                log_file_entity.close()

                if input() == 'y':
                    webbopen(
                        "https://gitee.com/meadeyetoe/simple_tools/releases/tag/v4.4-pre1")
                    return 1
                else:
                    return -3
            else:
                with open(f"simple_tools-{new_info['version']}.zip", 'wb') as package:
                    package.write(req.content)
        else:
            print('自动更新已取消\n你可以稍后进行手动更新\nGitHub: https://github.com/8388688/simple_tools\n'
                  'Gitee: https://gitee.com/meadeyetoe/simple_tools/releases/tag/v4.4-pre1\n'
                  '蓝奏云: \n1. https://imagine-8.lanzoue.com/ie3SB0mjnlsj\n'
                  '2. https://lanzoux.com/ie3SB0mjnlsj')
    else:
        print("暂无更新。")


def is_exec():
    return hasattr(sys, '_MEIPASS')


if __name__ == '__main__':
    get_update()
    if input("擦除缓存？<Any>/<Empty>"):
        clear_module_cache()
    else:
        print("canceled.")
