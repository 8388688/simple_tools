文件更新日志
==========

[changelog]: changelog.md

[data_base]: data_base.py

[data_process]: data_process.py

[default]: misc.py

[encr_decr]: encr_decr.py

[example]: example.py

[game_disposition]: game_disposition.py

[gui_extend]: gui_extend.py

[hash]: hash.py

[LICENSE]: LICENSE

[maths]: maths.py

[randoms]: randoms.py

[README]: README.md

[system_extend]: system_extend.py

[times]: times.py

[version]: version.json

[__init__]: __init__.py

* 4.x
    * 4.7 更新 \[**简并更新**\]:
        * 4.7 Release
            * 2025-07-22
            * 移除了几乎所有的 I/O 操作（现在不再在 %APPDATA% 下自动创建无用的文件夹了）
            * list2str 现已弃用，预计下个版本（4.8）移除
            * encr_decr.py: 移除 absolute_encryption, file_encryption, normal_encryption, normal_encryption_with_bytes
            * game_disposition.py: 移除 Person，弃用 Users 并移除相关代码，预计下个版本（4.8）移除 game_disposition.py 本体
            * 移除 decomposition 的安全锁功能
            <!-- 以下为 2025-03-15 修改 -->
            * Deleted: 彻底移除 `convert_system()` 函数
            * Modified: 改进 tree_fp_gen 函数
            * Fixed: fp_gen 在 files=true, folders=false 时，无论 skip_sl 设置为何值都无法输出符号链接
        * 4.7-pre2 \[2025-02-03-20-42-43\]
            * Modified: 移除 [randoms][randoms] 中的 `create_random_list` 的 `returns=True` 参数，一律使用返回值。
            * Fixed: `filter_()` 函数 `"float"` 模式无法启用 `"unsigned"` 参数。
            * Modified: dimensional_list 现在将返回一个生成器而不是列表。
            * Fixed: `deprecated()` 函数用 warnings 修饰。
        * 4.7-pre1 \[2024-10-04-20-15-07\]
            * Deleted: 移除 [system_extend][system_extend] 中的 `File` 类
            * Modified: 优化 `fp_gen()` 函数
    * 4.6 更新 \[**简并更新**\]:
        * 4.6 Release \[2024-07-15-17-27-57\] \(version_code: 20240715001\)
            * Updated: `get_fname()` 添加 `expert_mode` 参数，此参数控制输出方式（简单模式/专家模式），默认为 False（简单模式）。
            * Updated: `fp_gen()` 添加“专家模式”输出方式 `abspath=-1`。
            * Renamed: `file_remove() -> del_tree()`
            * Modified: 删除 `safe_md()` 的文件日志记录相关的代码。
            * Deleted: 清空 `normal_encryption_with_bytes(), absolute_encryption(), file_encryption()` 三个函数的功能。
            * Fixed: 修复 `prime_range_gen()` 无法显示质数 2 的 bug。
        * 4.6-beta2 \[2024-06-27-22-44-32\] \(version_code: 20240627001\)
            * Modified: `scientific_notate()` 添加自定义列表
            * Fixed: 修复 `get_fname()` 没有添加进 [system_extend.\_\_all\_\_][system_extend] 的 bug
        * 4.6-beta1 \[2024-06-23-22-33-25\] \(version_code: 20240623001\)
            * Fixed: 修正若干拼写错误的变量名
            * Added: 添加 `gcd()` 函数
            * Deleted: 删除 `euclidean_algorithm()` 函数
            * Modified: 优化 import 语句，将所有的 `import ...` 全部改为 `from ... import ...`
            * Modified: 删除 [README.md][README] 中的版本提示
        * 4.6-pre2 \[2024-06-09-16-00-00\] \(version_code: 20240609001\)
            * Fixed: check_and_install_package 传入的第三方库已被安装时，无论 import_ 参数是否被设置为 True，都无法导入相关的库。
            * Fixed: 准备移除旧版本的 random_choice() 函数
            * Added: 加入新 random_choice() 函数（等概率随机抽取）
            * Modified: 加入 scientific_notate() 函数以替代 convert_system() 函数
            * Updated: 更新 [README.md][README]，删除“依赖的插件”中一些实际上并没有导入的包。
            * Modified: rename:
                * `get_time_stamp() -> timestamp()`
                * `get_fp_gen() -> fp_gen()`
                * `get_file_suffix() -> file_suffix()`
        * 4.6-pre1 \[2024-05-02-11-30-44\] \(version_code: 20240502001\)
            * Added: 添加 `tree_fp_gen()` 函数。
            * Fixed: 修正 `generate_prime_range()` 函数。
            * Updated: `decomposition()` display changed from 已完成 to 总进度。
            * Modified: 将 `generate_bl_properties`, `bl_properties` `bl_properties_test` 合并为 `bl_properties_gen`.
            * Fixed: 移除 `bl_properties_gen()` 对前置列表的依赖。
            * Deleted: 移除 `get_suffix` in [example][example].
            * Deleted: 清空 `review` 函数。
    * 4.5 更新: [程序规范化更新][__init__]
        * 4.5 Release \[2024-05-01-20-48-52\] \(version_code: 20240501001\)
            * Updated: Remove params 及其引用:
          ```python
          NULL = None
          EOF = -1
          null = 0
          ```
            * Deleted: [README][README] 文件中的部分死链接
            * Updated: [README][README] 文件格式
            * Updated: get_fp_gen() 三种输出模式：absolute path, filename, 相对内容根的路径。
            * Deleted: 移除 get_file_size() 函数。
            * Modified: 移除程序中无用的 import 语句。
        * 4.5-pre3 \[2024-02-15-11-10-33\] \(version_code: 20240215001\)
            * Fix: Create workspace in current directory when %APPDATA% is not defined.
            * 在 `check_and_install_package()` 函数中增加 noWarning 参数。
            * [data_process][data_process] 中加入 `equals_list()` 函数。
        * 4.5-pre2 \[2024-02-14-17-17-19\] \(version_code: 20240214001\)
            * 在 `check_and_install_package()` 函数中增加自动导入的功能。
            * 彻底移除 module1 旧版本的文件残留
            * \[[README]#_depend_on\]部分：增加 python.requests 依赖。
            * Rename: [hash_values.py][hash] -> [hash.py][hash]
            * Delete: filehistory.md
        * 4.5-pre1 \[2023-12-02-15-36-38\] \(version_code: 20231202001\)
            * Two functions (`get_file_path()` - `generate_file_path()`
              and `saving_decomposition()` - `decomposition()`) were merged.
            * 修改 `generate_file_path()` 函数的判定规则，使之匹配文件的规则更严格。
            * Rename 4 functions:
                ```
                generate_file_path() => get_fp_gen()
                get_file_path() => get_fp()
                decomposition() => decomposition_gui()
                saving_decomposition() => decomposition()
                ```
    * 4.4 更新: [版本自动升级更新][default]
        * Release 4.4 \[2023-03-25-16-25-56\] \(version_code: 20230225001\)
            * Rewrite of `search_to_str_in_list`, add two params named `recursion=False` and `insensitive_data=False`.
            * 简化 [example.py][example] 中的部分程序
            * Update `get_update()` function and rewrite the [`version.json`][version] file.
            * Update [README.md#你知道吗][README] plate.
            * > Add: Release 4.4 版本更新方面不兼容以前的所有版本.
        * 4.4-beta3 \[2023-01-19-14-25-50\] \(version_code: 20230219001\)
            * Update [README.md][README].
        * 4.4-beta2 \[2023-02-18-17-55-10\] \(version_code: 20230218001\)
            * Delete ~~passed.py~~.
            * Delete `breakpoint()` in passed.py.
            * Update `times.wait()`.
            * Move `passed.pass_()` to [default.py][default].
        * 4.4-beta1 \[2023-02-12-16-40-12\] \(version_code: 20230212001\)
            * Update `generate_file_path`, add a **Distributed operations** option
              and supplemented its documents.
            * Fix `get_time_stamp` a serious bug that make user use preset values compulsorily.
            * Download `version.json` to local.
        * 4.4-pre2 \[2023-02-03-21-35-38\] \(version_code: 20230203003\)
            * Add some error code in `get_update()`
            * Update `get_update()` as headers and mirror source code.
        * 4.4-pre1 \[2023-02-03-20-10-46\] \(version_code: 20230203002\)
            * Owned version code (yyyymmdd\<num\>)
              example: 20230203001
            * Auto upgrade itself
            * Publish [first release](https://github.com/8388688/simple_tools/releases/tag/4.4-pre1)
              on [GitHub](https://github.com/)
    * 4.3 更新: [简化更新][__init__]
        * 4.3 \[2023-02-03 18:08:59\] \(version_code: 20230203001\)
            * Remove `bl()`, `receive()`, `cacheTimes`, `money` (2 function, 2 variable).
            * Migrate `review()` as `review_2()`
            * Remove a few scripts that for test.
        * 4.3-alpha1 \[2023-01-31 20:21:59\]
            * Remove `bomb1()`, `bomb2()`, `create_toplevel()`,
              `draw1()`, `draw2()` (5 function).
            * Remove the tips of creating files.
            * Fix a bug: Repeat tip `<filepath> 文件不存在或已损坏\n正在重制此文件`.
              when the file `namelist.txt` was empty.
    * 4.2 更新: [maths 数学函数更新][maths]
        * 4.2-beta3 \[2023-01-26 11:11:20\]
            * Update `get_hash_values`, `get_md5`, add ratio-choice.
            * Delete 5 variables in [encr_decr][encr_decr].
        * 4.2-beta2 \[2023-01-24 17:53:05\]
            * Add `quiet` param to `normal_encryption_with_bytes`.
            * Migrate `normal_encryption` as `normal_encryption_with_byte`(constitutional with `class bytes`).
            * Fix `generate_prime_range` a tiny bug.
        * 4.2-beta1 \[2023-01-12 17:11:01\]
            * 用埃拉托斯特尼筛法重写 `get_prime_range()` 函数。
            * 修正 `is_prime()` 函数中 n=4 时返回 True 的 bug.
            * 发现 `generate_prime_range()` 函数的一个 bug.
    * 4.1 更新: [data_process 更新][data_process]
        * 4.1-pre4 \[2022-12-17 19:49:40\]
            * 合并 get_prime_range 和 generate_prime_range, 但仍保留 get_prime_range 作为一个匿名函数。
        * 4.1-pre3 \[2022-12-10 19:49:30\]
            * 让所有的目录在后台静默创建, 创建成功与否情况记录到对应的文件日志中。
            * 更新 dec_to_r_convert() 函数, 修正 强制将非数字字符转换成数字字符 的 bug.
        * 4.1-pre2 \[2022-11-20 19:31:26\]
            * 更新工作目录为 %APPDATA%\8388688\py_workspace\simple_tools (如下图)。
            ```
          from os import getenv, system, chdir as cd
          from os.path import join
          work_space = join(getenv('APPDATA'), '8388688', 'py_workspace', 'simple_tools')
          system('md ' + work_space)
          cd(work_space)
          ```
            * 对 encr_decr 中的函数重命名, 例如 'absoluteEncryption' -> 'absolute_encryption'. 同时, 为了防止老版本调用
              simple_tools 兼容性问题, 使用变量解决。
            * 更新 [changelog.md][changelog] 的文件链接格式。
          >     [README.md](README.md)
          >     ->
          >     [README]: README.md
          >     [README.md][README]
        * 4.1-pre1 \[2022-10-5 17:07:41\]
            * 修正 filter_ 中的一个 bug.
            * filter_ 自定义 walls.
            * 微调 [maths.py][maths] 中 saving_decomposition 函数。
    * 4.0 更新: \[[README.md][README] 更新\] \[20221003\]
        * 4.0 \[2022-10-5 15:26:54\]
            * 整理文件。
        * 4.0-pre3 \[2022-10-5 10:15:55\]
            * 重制 [README.md][README] (旧版本的自述文件请 ~~README_old.md~~)
            * 整理所有的 `if __name__ == '__main__':` 测试脚本到 [example.py][example] 中
        * 4.0-pre2 \[2022-10-4 09:13:20\]
            * merge files such as view.py, draw.py, bomb.py etc.
            * update [README.md][README]
            * update work space of simple_tools [%appdata%/simple_tools]
        * 4.0-pre1 \[2022-10-3 18:20:15\]
            * rename module1 to simple_tools
            * add files named [README.md][README] and [LICENSE][LICENSE]
            * upload these package to [GitHub](https://gitbub.com/)
            * 将 [\_\_init\_\_][__init__] 中的更新日志转移至 [README.md][README]
            * simple_tools 进入 Beta 版本
* 3.x
    * 3.4x
        * 3.4.6 更新: \[20220925\]
            * rename ~~review.py~~ to ~~view.py~~
            * 在 [system_extend.py][system_extend] 中修正一个很细微的 bug (打印无用的空行的 bug)
        * 3.4.5 更新: \[20220925\]
            * 优化 \_\_all\_\_ 变量, 整理内置文件
        * 3.4.4 更新: \[20220918\]
            * 修正 [system_extend.py][system_extend] 中一些错误
        * 3.4.3 更新: \[20220918\]
            * 在 [system_extend.py][system_extend] 中将 `from os import *` 更正为 `import os`
        * 3.4.2 更新: \[20220918\]
            * 优化 [data_handle.py][data_process] 和 [maths.py][maths] 函数名称
        * 3.4.1 更新: \[20220918\]
            * 优化程序结构\[下\]
        * 3.4 更新: [maths 数学函数更新][maths] \[20220918\]
            * 加入 getPrime 函数
            * rename getPrime to getPrimeRange,
            * 将 \[2\] 又改成 get_prime_range
            * 添加 get_prime_range_of_generator 函数
    * 3.3x
        * 3.3.8 更新: \[from 20220901 to 20220912\]
            * 优化程序结构\[中\]
        * 3.3.7 更新: \[20220825\]
            * 在 [default.py][default] 中加入 clear_module1_cache 函数
        * 3.3.6 更新: \[20220825\]
            * 优化程序结构\[上\]
        * 3.3.5 更新: \[20220824\]
            * rename maths.d() to maths.is_prime()
        * 3.3.4 更新: \[20220824\]
            * rename [encryption.py][encr_decr] to [encr_decr.py][encr_decr]
        * 3.3.3 更新: \[20220817\]
            * rename get_false_unix_time to get_time_stamp
        * 3.3.2 更新: \[20220817\]
            * (懒人福利)给 get_false_unix_time 增加 5 个预设值
        * 3.3.1 更新: \[20220817\]
            * 修复 [times.py][times] 中 get_false_unix_time 预设值下标越界的 bug
        * 3.3 更新: \[时间函数更新\] \[20220816\]
            * 大幅更新 get_false_unix_time
                * 准备了 1,133,180,928 种不同的时间戳格式, 打造自己独一无二的时间戳
                * \(懒人福利\)自动设置默认时间格式
                * 修复程序一堆诡异的 bug
    * 3.2x
        * 3.2.2 更新: \[20220816\]
            * 加入 get_false_unix_time properties 更多装饰格式
        * 3.2.1 更新: \[20220815\]
            * 修复 [system_extend.py][system_extend] 中 get_file_name 函数写入日志时遇到中文会显示乱码的情况
        * 3.2 更新: \[文件系统 - 工作目录更新\] \[20220815\]
            * 给每个文件都配置了相应的工作目录
            * 存储在 [AppData/Roaming/module1](%appdata%/Roaming/module1) 中
            * 修正模块循环导入的 ImportError
    * 3.1x
        * 3.1 更新: [system_ 更新][system_extend] \[20220815\]
        * rename [system_.py][system_extend] 为 [system_extend.py][system_extend]
        * 在 [system_extend.py][system_extend] 中添加 safe_md 函数
    * 3.0x
        * 3.0.2 更新: \[20220815\]
            * 更新 [maths.py][maths] 的 decomposition 函数
        * 3.0.1 更新: \[20220814\]
            * 修复 ~~bomb.py~~ 的一个 bug
        * 3.0 更新: [文件系统更新] \[20220814\]
            * 拥有了自己的工作目录: [%APPDATA%/module1](%APPDATA%/module1)
            * 自动生成工作目录
            * 添加 MODULE1_WORK_SPACE 常量, 用于声明工作目录
* 2.x
    * 2.9x
        * 2.9.1 更改: \[20220814\]
            * 修复 [game_disposition.py][game_disposition] 中 Users 类的少量 bug
        * 2.9 更改: [game_disposition 更新][game_disposition] \[20220813\]
            * 大规模更新 [game_disposition.py][game_disposition] 中的 Users 类
                * 用户
                    * 用户体验
                        * 退出时将用户信息存储到文件中
                        * 现在登陆时需要密码
                        * 加入 logout 退出函数
                        * 离线用户在退出时自动清理数据
                * 用户安全
                    * topUp 等应用函数会拒绝 temporary 临时用户的访问
                    * \_\_del\_\_ 析构函数会拒绝 self.live 为 False 用户的访问
                * 安全: \[使用更安全的 uid\]
                    * 生成方式: 使用 md5 生成(通常的 uuid4)
                    * 在程序中以 `self.info_dict['uid']` 的形式存储
                    * 代替用户的 name 作为唯一的 ID
                    * 单独存储, 比 name 更安全
                * 程序
                    * 加入一些常量
                    * 优化原来的程序结构
                    * 修复一堆 bug
                    * 加入重制文件的功能
                    * 自动检测损坏的文件
                * 太多了, 说不过来了. . .
    * 2.8x
        * 2.8.4 更改: \[20220813\]
            * 修复 get_file_path_of_generator 区分大小写出错的 bug
        * 2.8.3 更改: \[20220812\]
            * 给 get_file_path_of_generator 添加 case_sensitive 限制条件
        * 2.8.2 更改: \[20220812\]
            * 更新 [data_handle][data_process] 的 \_\_all\_\_ 变量
        * 2.8.1 更改: \[20220812\]
            * 删除 ~~review.py~~ 下的 bl_generator 函数
        * 2.8 更改: [程序结构更新] \[20220812\]
            * 新建 [game_disposition.py][game_disposition] 文件
            * 将 User 类 和 Person 类 移到 [game_disposition.py][game_disposition] 中
            * 删除 [\_\_init\_\_.py][__init__] 中一些无用的引用
            * 更新 [\_\_init\_\_.py][__init__] 的注释
    * 2.7x
        * 2.7.3 更改: \[20220810\]
            * 删除 [system_.py][system_extend] 中的 get_file_name_of_generator 生成器
        * 2.7.2 更改: \[20220810\]
            * 在 [hash_values.py][hash] 中加入 uuid_generator 函数
        * 2.7.1 更改: \[20220810\]
            * 在 [system_.py][system_extend] 中, 将 get_file_name_of_generator 与 get_file_path_of_generator 合并
        * 2.7 更改: [system_ 更新][system_extend] \[20220809\]
            * 更新 get_file_name
                * 加入生成错误日志的功能
                * 加入 OSError 错误类型
            * file_pattern 加入文件路径无法识别的错误类型
            * 更新 get_file_path_of_generator 函数, 修正其中几个 bug
            * 为 get_file_path_of_generator 添加 include 和 exclude 限制条件
            * 大规模更新 File 类, 添加 permission, user_id 等 10 多种属性
    * 2.6x
        * 2.6.1 更改: \[20220801\]
            * normalEncryption 的 coding 参数 现在可选项为 `[getfilesystemencoding(), 'utf-8', 'gbk']`
        * 2.6 更改: [加密更新][hash] \[20220801\]
            * 更新 md5_encryption
            * 修正 normalEncryption 的 bug
            * 更新 normalEncryption, 加入 coding 参数 `['auto', 'f_byte', 'f_int']` 三个可选项
    * 2.5x
        * 2.5.1 更改: \[20220727\]
            * 加入 md5_encryption
            * 更新 normal_encryption 函数, 修复一些 bug
            * 更新 [更新日志][changelog] 的体制
        * 2.5 更改: [system_ 更新][system_extend] \[20220404\]
        * 在 [system_.py][system_extend] 下创建 File 类
        * 添加 system_pro 变量声明当前操作系统
    * 2.4x
        * 2.4.4 更改: \[20220320\]
            * 创建 [example.py][example] 文件
            * \[时间中断\]
        * 2.4.3 更改: \[20220312\]
            * 修正 get_file_path_of_generator 无法返回所有文件夹的 bug
            * 更新 file_remove, get_file_name, file_pattern
        * 2.4.2 更改: \[20220305\]
            * 添加 random_choice 函数
        * 2.4.1 更改: \[20220305\]
            * 删除 create_random 变量
            * 更新 file_pattern 函数, 添加 easy_options 参数
        * 2.4 更改: [times 更新][times] \[20220305\]
            * 创建 [times.py][times] 文件
            * 在 [times.py][times] 中创建 get_false_unix_time 函数
            * 移动 wait 函数到 [times.py][times] 中
            * 更新 [\_\_init\_\_.py][__init__] 的 \_\_all\_\_ 变量
    * 2.3x
        * 2.3.1 更改: \[20220226\]
            * 创建 [hash_values.py][hash] 文件
            * 把 get_md5 函数移到 [hash_values.py][hash] 下
        * 2.3 更改: [data_handle 更新][data_process] \[20220226\]
            * 更新并完善 filter_ 的 other_signs 参数
            * 在 [data_base.py][data_base] 中加入 tabs 元组
            * 更新 \_\_all\_\_ 变量
    * 2.2x
        * 2.2.3 更改: \[20220219\]
            * 更新 filter_ 的 other_signs 参数
            * 删除 test() 中的 draw1 引用
        * 2.2.2 更改: \[20220219\]
            * 加入 binarySearch 函数
        * 2.2.1 更改: \[20220205\]
            * rename username to usernameList
        * 2.2 更改: \[20220205\]
            * rename str_handle to data_handle
            * 删除 default 中的 createToplevel
            * 创建 [test.py](example.py)
    * 2.1x
        * 2.1 更改: \[20220203\]
            * 更新 file_remove 函数无法删除文件夹的 bug
            * 增加 file_pattern 函数.
            * 在 [system_.py][system_extend] 中添加 `fp = getcwd()` 常量
            * 创建 dimensionalList 在 [data_handle.py][data_process]
    * 2.0x
        * 2.0.1 更改: \[20220203\]
            * 修正模块常量无法导入的问题
        * 2.0 更改: \[20220203更早, 下同\]
            * 创建 file_remove, 大规模升级 [system_.py][system_extend]
            * 修正 get_file_path_of_generator 的 bug
            * 加入常量 `EOF = -1, NULL = None, null = 0`
            * 删除 [\_\_init\_\_.py][__init__] 的 absoluteEncryption
            * 创建 [data_base.py][data_base] 数据库.
* 1.x
    * 1.8x
        * 1.8 更改:
            * 创建 [system_.py][system_extend]
            * 移动 get_file_name, get_file_name_of_generator,get_file_path, get_file_path_of_generator,
              get_file_size,get_files, get_file_names 到 [system_.py][system_extend]
    * 1.7x
        * 1.7.1 更改:
            * 更新 Users,
            * pw 用 md5 加密.
        * 1.7 更改:
            * 删除 [\_\_init\_\_.py][__init__] 的 review, digitalDecryption, draw1, draw2, breakpoint_
            * 修正 breakpoint_ 中 exit_ 的 bug
            * 创建 [randoms.py][randoms] 并添加 createRandomList
            * 删除 [\_\_init\_\_.py][__init__] 的 passed, EuclideanAlgorithm.
    * 1.6x
        * 1.6.13 更改:
            * 修正 get_file_path 的 bug.
        * 1.6.12 更改:
            * 给 get_file_name 添加注释.
        * 1.6.11 更改:
            * 1.更新 username 词库
            * 2.修改随机起名的 bug.
        * 1.6.10 更改:
            * 1.更新 filter_ R 进制过滤的 bug
            * 2.把 get_files 改名为 get_file_path.
        * 1.6.9 更改:
            * 1.更新 EuclideanAlgorithm
            * 2.删除 [\_\_init\_\_.py][__init__] 的 bl.
        * 1.6.8 更改:
            * 1.把 divisionAlgorithm 函数更名为 EuclideanAlgorithm,
            * 2.删除 [\_\_init\_\_.py][__init__] 的 conversionSystem.
        * 1.6.7 更改:
            * 加进 get_file_name 和 get_files 两个函数在 default.py 中.
