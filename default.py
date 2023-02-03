from requests import get

from simple_tools.data_base import ST_WORK_SPACE, fp
from simple_tools.system_extend import delete

__all__ = ['get_update']
__version__ = '4.3'
version_code = 20230203001


def clear_module_cache():
    delete(ST_WORK_SPACE)


def get_update():
    new_info = get(r'https://raw.githubusercontent.com/8388688/simple_tools/data/version.json').json()

    if new_info['version_code'] > version_code:
        print('有新版本可用：', new_info['version'], '（当前版本', __version__, '），更新内容：')
        for v in new_info['updatecontent']:  # 输出更新内容
            if new_info['updatecontent'][v][0] <= version_code:
                break
            print('└- ' + v + '：' + new_info['updatecontent'][v][1])
        print('请手动打开 https://github.com/8388688/simple_tools 更新')
        '''
        print("更新完成，重启程序生效！")
        exit()
        '''


if __name__ == '__main__':
    get_update()
