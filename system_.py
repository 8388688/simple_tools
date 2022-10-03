from os import *

from module1 import NULL
from module1.times import wait
from stat import *

__all__ = ['fp', 'delete', 'get_files', 'get_file_names',
           'file_pattern', 'file_remove', 'get_file_name',
           'get_file_name_of_generator', 'get_file_path',
           'get_file_path_of_generator', 'get_file_size',
           'get_file_suffix']

fp = getcwd()


def file_pattern(file_path=fp, binary=True, easy_options=False):
    """判断一个 file 类型

    文件代码：
    -3 = 拒绝访问
    -2 = 找不到文件
    -1 = 未知的错误
    1 = 空文件夹
    2 = 不是空的文件夹
    3 = 空文件
    4 = 不是空的文件

    :param file_path: 文件路径
    :param binary: 数字返回/模拟返回，默认为数字返回
    :param easy_options: 使函数返回简单的 True/False 值而不是更高级的返回方式
    :return: 未知
    """
    key_val = {1: ('空文件夹',), 2: ('不是空的文件夹',), 3: ('空文件',), 4: ('不是空的文件',),
               -1: ('未知的错误',), -2: ('找不到文件',), -3: ('拒绝访问',), -4: ('内置错误',)}
    nor_code = (1, 2, 3, 4,)
    problem_code = (-3, -2, -1,)
    button = -1
    if path.exists(file_path):
        if path.isfile(file_path):
            if path.getsize(file_path) <= 1:
                button = 3
            else:
                button = 4
        else:
            try:
                listdir(file_path)
            except PermissionError:
                button = -3
            else:
                if listdir(file_path):
                    button = 2
                else:
                    button = 1
    else:
        button = -2

    if easy_options:
        if button in nor_code:
            return True
        elif button in problem_code:
            return False
        else:
            return None
    else:
        if binary:
            return button
        else:
            return key_val.get(button, key_val.get(-4))


def file_remove(file_path=fp, all_files=False, all_folders=False,
                forces=False, confirms=False, quiet=False, **kwargs):
    """删除一个或多个文件

    :param file_path: 指定的文件路径，可以是文件，也可以是文件夹。
    :param all_files: 如果 file_path 指定了一个文件夹，这个参数将会删除 file_path 中的所有指定的文件。
    :param all_folders: 如果 file_path 指定了一个文件夹，这个参数将会删除 file_path 中的所有指定的子文件夹。
    :param forces: 强制删除只读文件.
    :param confirms: 删除每一个文件之前提示确认.
    :param quiet: 安静模式(此参数与 confirms 参数不能同时为 True)。
    :return: 如果删除成功的话返回 0，否则返回非0值
    """

    new_path = file_path  # 文件路径
    delete_dir = True

    for a000 in get_file_path_of_generator(new_path, abspath=True, all_files=all_files, folders=all_folders):
        if path.exists(a000):  # 如果文件存在
            if confirms:
                select = input('确定删除%s吗?(<Any> or <space>)' % a000)
            else:
                select = True
            if select:
                # 删除文件，可使用以下两种方法。
                if forces:
                    chmod(a000, S_IWRITE)
                if not quiet:
                    print('删除文件 - %s' % a000)
                if path.isfile(a000):
                    remove(a000)
                    # os.unlink(path)
                elif all_folders:
                    rmdir(a000)
                else:
                    print('跳过%s' % a000)
                    delete_dir = False
            else:
                print('操作已取消')
                delete_dir = False
        else:
            print('错误 - 找不到\"%s\"' % a000)  # 否则返回文件不存在
            delete_dir = False
            return 1

    if delete_dir:
        rmdir(new_path)
    return 0


def get_file_name(file_dir=fp):
    key_val = (('出错了(未知的错误)', []),
               ('出错了(内置错误: 未知)', []),
               ('出错了(内置错误: 下标越界)', []),
               ('出错了(找不到文件)', []),
               ('保留位置', []),
               ('出错了(拒绝访问)', []),
               ('出错了(unicode编码错误)', []))
    button = 0
    if path.isfile(file_dir):
        return []
    else:
        try:
            return listdir(file_dir)
        except FileNotFoundError:
            button = 3
            print('%s\"%s\"' % (key_val[button], file_dir))
            return []
        except PermissionError:
            button = 5
            print('%s\"%s\"' % (key_val[button], file_dir))
            return []
        except UnicodeEncodeError:
            button = 6
            print('%s\"%s\"' % (key_val[button], file_dir))
            return []
        except IndexError:
            button = 2
            print('%s\"%s\"' % (key_val[button], file_dir))
            return
        except:
            button = 1
            print('%s\"%s\"' % (key_val[button], file_dir))


def get_file_name_of_generator(file_path=fp, abspath=False, folders=False):
    """获取文件名

    输出时检测如果是一个文件夹，就以列表的格式输出，否则以str的格式输出

    :param file_path: 目标文件或路径
    :param abspath: 使用绝对路径
    :param folders: 也输出文件夹
    :return: 如果是一个目录就以列表的格式输出，否则以str的格式输出

    """
    fx = get_file_name(file_path)

    for file in fx:
        if path.isfile(path.join(file_path, file)):
            if abspath:
                yield str(path.join(path.abspath(file_path), file))
            else:
                yield str(file)
        else:
            for a000 in get_file_name_of_generator(path.join(file_path, file)
                                                   + '\\', abspath=abspath):
                yield a000
            if folders:
                yield path.join(file_path, file)


def get_file_path(file_path=fp, abspath=False, folders=False, format_list=False, **kwargs):
    """获取文件路径

    输出时检测如果是一个文件夹，就以列表的格式输出，否则以str的格式输出

    :param file_path: 目标文件或路径
    :param abspath: 使用绝对路径
    :param folders: 也输出文件夹
    :param format_list: 输出时强制转换成列表格式
    :param kwargs: 高级选项：
    \n from_size: 限制文件大小下限
    \n to_size: 限制文件大小上限
    \n suffix: 限制文件后缀名(不加“.”)
    :return: 如果是一个目录就以列表的格式输出，否则以str的格式输出

    """
    files = []
    fx = get_file_name(file_path)
    extension = kwargs
    from_size = extension.get('from_size', 0)
    to_size = extension.get('to_size', NULL)
    suffix = extension.get('suffix', NULL)
    # extension.get('', default=NULL)

    for file in fx:
        if path.isfile(path.join(file_path, file)):
            if (to_size is NULL or path.getsize(path.join(file_path, file)) < to_size) \
                    and from_size < path.getsize(path.join(file_path, file)) and \
                    (suffix is NULL or path.join(file_path, file).split('.')[-1] == suffix):
                if abspath:
                    files.append(str(path.join(path.abspath(file_path), file)))
                else:
                    files.append(str(path.join(file_path, file)))
        else:
            if format_list:
                for i in get_file_path(path.join(file_path, file) + '\\', abspath=abspath, format_list=format_list,
                                       from_size=extension.get('from_size', 0), to_size=extension.get('to_size', NULL),
                                       suffix=extension.get('suffix', NULL)):
                    files.append(i)
                if folders:
                    files.append(path.join(file_path, file))
            else:
                files.append(get_file_path(path.join(file_path, file) + '\\', abspath=abspath, format_list=format_list,
                                           from_size=extension.get('from_size', 0),
                                           to_size=extension.get('to_size', NULL),
                                           suffix=extension.get('suffix', NULL)))

    if path.isfile(file_path):
        if abspath:
            return path.abspath(file_path)
        elif format_list:
            return [file_path, ]
        else:
            return file_path
    else:
        if format_list:
            return [files, ]
        else:
            return files


def get_file_path_of_generator(file_path=fp, abspath=False, folders=False, __deep=0, **kwargs):
    """获取文件路径

    输出时检测如果是一个文件夹，就以列表的格式输出，否则以str的格式输出

    :param file_path: 目标文件或路径
    :param abspath: 使用绝对路径
    :param folders: 也输出文件夹
    :param kwargs: 高级选项：
    \n from_size: 限制文件大小下限
    \n to_size: 限制文件大小上限
    \n suffix: 限制文件后缀名(不加“.”)
    :return: 如果是一个目录就以列表的格式输出，否则以str的格式输出

    """
    fx = get_file_name(file_path)

    extension = kwargs
    from_size = extension.get('from_size', 0)
    to_size = extension.get('to_size', NULL)
    suffix = extension.get('suffix', NULL)
    # extension.get('', default=NULL)

    for file in fx:
        if path.isfile(path.join(file_path, file)):
            if (to_size is NULL or path.getsize(path.join(file_path, file)) < to_size) \
                    and from_size < path.getsize(path.join(file_path, file)) and \
                    (suffix is NULL or path.join(file_path, file).split('.')[-1] == suffix):
                if abspath:
                    yield str(path.join(path.abspath(file_path), file))
                else:
                    yield str(path.join(file_path, file))
        else:
            for a000 in get_file_path_of_generator(path.join(file_path, file) + '\\',
                                                   abspath=abspath, folders=folders,
                                                   from_size=from_size, to_size=to_size,
                                                   suffix=suffix):
                yield a000
            if folders:
                yield path.join(file_path, file)


def get_file_size(path_var=fp, all_files=True, details=False, **kwargs):
    extension = kwargs
    from_size = extension.get('from_size', 0)
    to_size = extension.get('to_size', NULL)
    suffix = extension.get('suffix', NULL)
    # extension.get('', default=NULL)

    size, files, folders = 0, 0, 0
    if path.isdir(path_var):
        for i in listdir(path_var):
            path_new = path.join(path_var, i)
            if path.isfile(path_new):
                if (to_size is NULL or path.getsize(path.join(path_var, i)) < to_size) \
                        and from_size < path.getsize(path.join(path_var, i)) and \
                        (suffix is NULL or path.join(path_var, i).split('.')[-1] == suffix):
                    files += 1
                    size += path.getsize(path_new)
            elif all_files:
                folders += 1
                gfs = get_file_size(path_new, True, True, from_size=from_size, to_size=to_size, suffix=suffix)
                size += gfs[0]
                files += gfs[1]
                folders += gfs[2]
            else:
                print(path_new, '是文件夹')
    else:
        files += 1
        size += path.getsize(path_var)
    if details:
        return size, files, folders
    else:
        return size


def get_file_suffix(file_path=fp, sort=True, show_details=False):
    fp_ = file_path
    keys = []

    for i in get_file_name_of_generator(fp_, False):
        keys.append(str.lower(i.split('.')[-1]))
        if show_details:
            print(i)

    if sort:
        keys = sorted(list(set(keys)))
    return keys


delete = file_remove
get_files = get_file_path_of_generator
get_file_names = get_file_name_of_generator

if __name__ == '__main__':
    for k in get_file_path_of_generator('C:\\', True, from_size=1000, to_size=1000000,
                                        suffix='exe'):
        print(k)
