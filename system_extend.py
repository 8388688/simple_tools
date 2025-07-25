import os
import stat
from random import randrange
# from stat import *
from sys import getdefaultencoding as gde
from traceback import format_exc

from simple_tools.data_base import pass_, tabs_bl
from simple_tools.times import timestamp as gettime
from simple_tools.misc import deprecated, invoke

__all__ = [
    "fp",

    "file_pattern", "del_tree", "get_file_name", "get_fname",
    "get_fp", "fp_gen",
    "quick_create_file", "safe_delete", "tree_fp_gen",
    "listdir_p_gen", "listdir_p",

    "delete", "get_files", "generate_file_path", "file_remove",
    "get_file_path"
]


fp = os.getcwd()


def file_pattern(file_path=fp, binary=True, easy_options=False):
    """判断一个 file 类型

    文件代码：
    -5 = 内存不足
    -4 = 内置错误
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
               -1: ('错误 - 未知的错误',), -2: ('错误 - 找不到文件',), -3: ('错误 - 拒绝访问',), -4: ('内置错误',),
               -5: ('错误 - 内存不足',), -6: ('错误 - 文件路径无法识别',)}
    nor_code = (1, 2, 3, 4,)
    problem_code = (-6, -3, -2, -1,)
    undef_code = (-4, -5)
    button = -1
    now_fp = fp
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            if os.path.getsize(file_path) <= 1:
                button = 3
            else:
                button = 4
        elif os.path.isdir(file_path):
            try:
                os.listdir(file_path)
            except PermissionError:
                button = -3
            except MemoryError:
                button = -5
            else:
                if os.listdir(file_path):
                    button = 2
                else:
                    button = 1
        else:
            button = -6
    else:
        if len(file_path) >= 255:
            button = -6
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


def del_tree(file_path=fp, all_files=False, all_folders=False,
             forces=False, confirms=False, quiet=False, **kwargs):
    """删除一个或多个文件

    :param file_path: 指定的文件路径，可以是文件，也可以是文件夹。
    :param all_files: 如果 file_path 指定了一个文件夹，这个参数将会删除 file_path 中的所有指定的文件。
    :param all_folders: 如果 file_path 指定了一个文件夹，这个参数将会删除 file_path 中的所有指定的子文件夹。
    :param forces: 强制删除只读文件.
    :param confirms: 删除每一个文件之前提示确认.
    :param quiet: 安静模式(此参数与 confirms 参数不能同时为 True)。
    :return: 如果删除成功的话返回 0，否则返回非 0 值
    """

    new_path = file_path  # 文件路径
    delete_dir = True

    def only_remove(file_or_dir):
        nonlocal delete_dir
        if not os.path.exists(file_or_dir) and os.path.exists(file_or_dir + os.sep):
            only_remove(file_or_dir + os.sep)
            print("Windows 特色畸形文件 - %s" % file_or_dir)
            return "Windows 特色畸形文件 - %s" % file_or_dir
        if os.path.exists(file_or_dir):  # 如果文件存在
            if confirms:
                select = input('确定删除%s吗?(<Any> or <space>)' % file_or_dir)
            else:
                select = True
            if select:
                # 删除文件，可使用以下两种方法。
                if forces:
                    os.chmod(file_or_dir, stat.S_IRWXU)
                    os.chmod(file_or_dir, stat.S_IWRITE)
                if not quiet:
                    print('删除文件 - %s' % file_or_dir)
                if os.path.isfile(file_or_dir):
                    os.remove(file_or_dir)
                    # unlink(path)
                elif all_folders:
                    try:
                        os.rmdir(file_or_dir + os.sep)
                    except NotADirectoryError:
                        print("WARNING: 出现一个与目标文件夹名称相同的非文件夹")
                        os.remove(file_or_dir)
                else:
                    print('跳过%s' % file_or_dir)
                    delete_dir = False
            else:
                print('操作已取消')
                delete_dir = False
        else:
            print('错误 - 找不到 \"%s\"' % file_or_dir)  # 否则返回文件不存在
            delete_dir = False
            # return 1

    for a000 in fp_gen(new_path, abspath=1, folders=all_folders, all_files=all_files, do_file=lambda f: only_remove(f),
                       do_dir=lambda f2: only_remove(f2)):
        # print('将要删除的文件:', a000, 'Size:', getsize(a000))
        pass_()

    if delete_dir:
        only_remove(new_path)
    return 0


def get_fname(file_dir=fp, command=os.listdir, expert_mode=False):
    key_val = (('命令成功完成', []),
               ('出错了(未知错误)', []),
               ('出错了(内置错误: 下标越界)', []),
               ('出错了(找不到文件)', []),
               ('保留位置', []),
               ('出错了(拒绝访问)', []),
               ('出错了(unicode编码错误)', []),
               ('出错了(系统无法辨识文件名)', []))
    button = 0

    # button > 0: 异常
    # button <= 0: 正常

    def _fprint(*args, step=' ', end='\n'):
        try:
            for string in args:
                print(str(string) + step, sep='', end='')
            print(end, end='')
        except UnicodeEncodeError:
            print('print() 函数似乎出现了错误')
            string = string.encode(gde())
            print(string)

    if os.path.isfile(file_dir):
        # return []
        return [file_dir, ] if not expert_mode else ([file_dir, ], button)
    else:
        try:
            ret = command(file_dir) if not expert_mode else (
                command(file_dir), button)
        except FileNotFoundError:
            button = 3
        except PermissionError:
            button = 5
        except UnicodeEncodeError:
            button = 6
        except IndexError:
            button = 2
        except OSError as e:
            # button = e.winerror
            button = 7
        except Exception as e:
            button = 1
        else:
            button = 0

        if button != 0:
            _fprint('%s\"%s\"' % (key_val[button], file_dir))
            _fprint(format_exc())
        if button == 0:
            return ret
        else:
            if expert_mode:
                return key_val[button][1], button
            else:
                return key_val[button][1]


def get_fp(file_path=fp, abspath=None, folders=False) -> tuple:
    import warnings
    warnings.warn(f"{deprecated(get_fp, fp_gen)} 此函数将在 4.9 版本移除",
                  PendingDeprecationWarning, stacklevel=4)
    print(f"{invoke(get_fp, fp_gen)}")
    print(f"\033[0;31m由于 {get_fp.__name__} 函数受 API 限制，无法启用过滤器。\033[0m")
    print(f"\033[0;31m推荐使用 {fp_gen.__name__} 函数。\033[0m")
    return tuple(fp_gen(file_path=file_path, abspath=abspath, folders=folders))


def fp_gen(file_path=fp, abspath=0, files=True, folders=False,
           __deep=0, **kwargs):
    """获取文件路径

    \n FIXME: get_fname() 对每一个文件夹重复运行两次，降低效率
    \n
    \n from_size: 限制文件大小下限
    \n to_size: 限制文件大小上限
    \n suffix: 限制文件后缀名(不加".")
    \n include: 包含的文件夹, (未指定就是全部)
    \n exclude: 排除的文件夹, (格式: 推荐元组, 但也可以用列表)
    \n case_sensitive: [针对 include]是否区分大小写, 默认为 False(不区分)
    \n do_file: 针对每一个文件要做什么
    \n do_dir: 针对每一个文件夹要做什么
    \n topdown: 如果此项被启用，那么输出时优先输出文件夹，否则优先输出文件。
    \n
    \n 当 file_path 被指定为单个文件时，只返回这个文件本身。
    \n 当 file_path 被指定为一个空文件夹时，不返回任何数据。
    \n
    \n 示例:
    \n
    \n ```python
    \n     # 删除 `H:/2020/Temp` 中的所有文件（文件夹）
    \n     for i in fp_gen('H:/2020/Temp', folders=True,
    \n                             do_file=lambda f: print(f, 'isfile:', os.path.isfile(f)),
    \n                             do_dir=lambda f2: print(f2, 'isdir:', os.path.isdir(f2))):
    \n         pass
    \n ```
    \n --------
    \n
    \n 或者是这样
    \n
    \n ```python
    \n     # 删除 `H:/2020/Temp` 中的所有文件（文件夹）
    \n     for i in fp_gen('H:/2020/Temp', folders=True,
    \n                             do_file=lambda f: os.unlink(f),
    \n                             do_dir=lambda f2: os.rmdir(f2)):
    \n         print('Delete file:', i)
    \n ```
    \n
    \n 空文件示例
    \n
    \n ```Python
    \n     for i in fp_gen('H:/2020/Temp/single.file'):
    \n         print(i)
    \n ```
    \n
    \n 输出结果:
    \n
    \n ```H:/2020/Temp/single.file```
    \n
    \n 空目录示例
    \n
    \n ```Python
    \n     for i in fp_gen('H:/2020/Temp/EmptyDir'):
    \n         print(i)
    \n ```
    \n
    \n 输出结果: ``` ```
    \n
    \n -----------
    \n abspath 示例:
    \n 0 = 自动判据
    \n 1 = True = absolute path
    \n 2 = False = filename
    \n 3 = 相对内容根的路径
    \n -1 = 以专家模式返回
    \n
    :param file_path: 目标文件或路径
    :param abspath: 使用绝对路径
    :param files: 是否输出文件
    :param folders: 是否输出文件夹
    :param __deep: 文件递归深度(未使用)
    :param kwargs: 高级选项:
    :return: 以列表的格式输出

    """

    # def yield_once():

    fx = get_fname(file_path, expert_mode=True)

    extension = kwargs
    # extension.get('', default=None)

    # 以下是正常的参数
    from_size = extension.get("from_size", 0)
    to_size = extension.get("to_size", None)
    suffix = extension.get("suffix", None)
    include = extension.get("include", [])
    exclude = extension.get("exclude", [])
    case_sensitive = extension.get("case_sensitive", False)
    do_dir_pre = extension.get("do_dir_pre", pass_)
    do_dir_later = extension.get("do_dir_later", pass_)
    # 0 = Exclude, 1 = Direct, 2 = Follow
    skip_symlink = extension.get("skip_sl", 2)
    from_root_fp = extension.get("__from_root_fp", "")

    # 以下为准备废弃的参数
    do_file = extension.get("do_file", pass_)
    do_dir = extension.get("do_dir", pass_)
    topdown = extension.get("topdown", extension.get("precedence_dir", False))

    for file in fx[0]:
        abs_fp_depart = (file_path, file, from_root_fp)
        abs_fp = os.path.join(abs_fp_depart[0], abs_fp_depart[1])
        if os.path.isfile(abs_fp) or ((os.path.islink(abs_fp) or os.path.isjunction(abs_fp)) and skip_symlink in [0, 1]):
            f_size = os.path.getsize(
                abs_fp) if os.path.isfile(abs_fp) else None
            if (os.path.islink(abs_fp) or os.path.isjunction(abs_fp)) and skip_symlink in [0, ]:
                continue
            elif (to_size is None or f_size is None or f_size < to_size) \
                    and (f_size is None or from_size <= f_size) and \
                    (suffix is None or abs_fp.split('.')[-1] == suffix or abs_fp.split('.')[-1] in suffix) and \
                    ((not include) or list(
                        filter(lambda pi: (pi in abs_fp) if case_sensitive else (pi.lower() in abs_fp.lower()),
                               include))) and \
                    ((not exclude) or not list(
                        filter(lambda pe: (pe in abs_fp) if case_sensitive else (pe.lower() in abs_fp.lower()),
                               exclude))):
                if abspath is True or abspath == 1:
                    yld = os.path.join(os.path.abspath(file_path), file)
                elif abspath is None or abspath == 0:
                    yld = abs_fp
                elif abspath is False or abspath == 2:
                    yld = file
                elif abspath == 3:
                    yld = os.path.join(abs_fp_depart[2], file)
                elif abspath == -1:
                    yld = (os.path.join(os.path.abspath(file_path), file), file, os.path.join(abs_fp_depart[2], file),
                           get_fname(abs_fp, expert_mode=True)[1])
                    # format: (<abspath>, <filename>, <相对内容根的路径>, <返回码: int>)
                else:
                    yld = abs_fp

                if files or ((os.path.islink(abs_fp) or os.path.isjunction(abs_fp)) and skip_symlink in [1, ]):
                    yield yld
                    do_file(yld)
                else:
                    pass
        else:
            if abspath is True or abspath == 1:
                yld = os.path.join(os.path.abspath(file_path), file)
            elif abspath is None or abspath == 0:
                yld = abs_fp
            elif abspath is False or abspath == 2:
                yld = file
            elif abspath == 3:
                yld = os.path.join(abs_fp_depart[2], file)
            elif abspath == -1:
                yld = (os.path.join(os.path.abspath(file_path), file), file, os.path.join(abs_fp_depart[2], file),
                       get_fname(abs_fp, expert_mode=True)[1])
                # format: (<abspath>, <filename>, <相对内容根的路径>, <返回码: int>)
            else:
                yld = abs_fp

            if folders:
                do_dir_pre(yld)
            can_yield = ((not include) or list(
                filter(lambda pi: (pi in abs_fp) if case_sensitive else (pi.lower() in abs_fp.lower()),
                       include))) and ((not exclude) or not list(
                           filter(lambda pe: (pe in abs_fp) if case_sensitive else (pe.lower() in abs_fp.lower()),
                                  exclude)))
            if folders and topdown and can_yield:
                yield yld
                do_dir(yld)
            temp_kwargs = kwargs
            temp_kwargs.update(
                {"__from_root_fp": os.path.join(from_root_fp, abs_fp_depart[1])})
            for a000 in fp_gen(abs_fp + os.sep, abspath=abspath, files=files, folders=folders, **temp_kwargs):
                yield a000

            if folders:
                do_dir_later(yld)
            if folders and not topdown and can_yield:
                yield yld
                do_dir(yld)


def quick_create_file(file_path, size):
    fx = open(file_path, 'wb')
    fx.seek(size - 1)
    fx.write(b'\x00')
    fx.close()


def safe_delete(file_path, buffering=16777216):
    for i in fp_gen(file_path, folders=False):
        size = os.path.getsize(i)
        file = open(i, "w", buffering=buffering)
        while size > 0:
            print("生成字节")
            buffer = ""
            # # # # # mode 1
            for char in range(min(size, buffering)):
                buffer += chr(randrange(32, 127))
            # # # # # mode 2
            # buffer = "\0" * buffering
            # # # # # mode 3
            # buffer = chr(randrange(32, 127)) * buffering
            # # # # # mode 4 FIXME: 统计字节
            # for seq in range(min(size, buffering)):
            #     range_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
            #     shuffle(range_list)
            #     print(f"{range_list=}")
            #     for char in range_list:
            #         buffer += char

            print('填充文件. . .')
            file.write(buffer)
            size -= len(buffer)
        file.close()
        new_name = os.path.join(
            os.path.dirname(i), "RUN_AWAY.txt" +
            gettime(no_beauty=True, idiotMode=False,
                                pf_year=1, pf_month=1, pf_day=1, pf_hour=1, pf_minute=1, pf_second=1))
        os.rename(i, new_name)
        os.remove(new_name)
        print('COMPLETE! - %s => %s' % (i, new_name))


def tree_fp_gen(__fp, files=True, header=None, __prefix="", keepend=True):
    bucket_fname = os.listdir(__fp)
    bucket_fp = [os.path.join(__fp, x) for x in bucket_fname]
    suffix = "\n" if keepend else ""
    if not __prefix:
        if header is None:
            header = __fp
        yield header + suffix
    for i in range(len(bucket_fp)):
        decorate = __prefix
        if i + 1 == len(bucket_fp):
            dec_presets = tabs_bl[0]
        else:
            dec_presets = tabs_bl[1]

        yld = decorate + dec_presets[0] + bucket_fname[i]
        if os.path.isdir(bucket_fp[i]):
            yield yld + "<dir>" + suffix
            for item in tree_fp_gen(bucket_fp[i], files=files, __prefix=decorate + dec_presets[1]):
                yield item
        elif files:
            yield yld + suffix
        else:
            pass


def listdir_p(__fp):
    return list(listdir_p_gen(__fp))


def listdir_p_gen(__fp):
    for i in os.listdir(__fp):
        yield os.path.join(__fp, i)


delete = file_remove = del_tree
get_file_path = get_fp
get_files = generate_file_path = get_fp_gen = fp_gen
get_file_name = get_fname
