# simple_tools - һ���� python д�ļ��׹��߰�

-----
<span id="menu">����:</span>

1. [����](#menu)
2. [����](#summary)
3. [�ļ�](#projects)
4. [�����Ĳ��](#depend_on)
5. [bug׷��](#bug_report)
6. [��һ���汾��Ԥ��](#next_version)
7. [������־](#update_log)
8. [�ļ���ʷ��¼](#file_history)
9. [��֪����](#do_you_know)

-----
<span id="summary">����</span>

[�ص�����](#menu)

## ����

������: �زĴ�Ӫ

����: 8388688

version: Beta 4.0-pre3

����޸�ʱ�䣺2022-10-5 10:17:57

[��Ч]~~����ļ��������ܳ��� 270 ��~~

1.6.6 ��ǰ�İ汾ȫ����, �޷���ȡ��

All versions of module1 before 1.6.6 are broken and can't be read.

2.0.1 ��ǰ�İ汾�������޸ĺͷ���ʱ����̫��, ������, �޷���ȡ��

Version 2.0.1 before create, modify,

and access time interval is too long,

was serious damaged and can't read

-----
<span id="projects">�ļ�</span>

[�ص�����](#menu)

## �ļ�

[data_base]: data_base.py

[data_process]: data_process.py

[default]: default.py

[encr_decr]: encr_decr.py

[example]: example.py

[game_disposition]: game_disposition.py

[gui_extend]: gui_extend.py

[hash_values]: hash_values.py

[LICENSE]: LICENSE

[maths]: maths.py

[passed]: passed.py

[randoms]: randoms.py

[README]: README.md

[README_old]: README_old.md

[system_extend]: system_extend.py

[times]: times.py

[__init__]: __init__.py

-----
<span id="depend_on">�����Ĳ��</span>

[�ص�����](#menu)

## �����Ĳ��

[TOC]

* python.io
* python.math
* python.os
* python.random
* python.stat
* python.sys
* python.tkinter
* python.turtle
* . . . . . .

-----
<span id="bug_report">bug׷��</span>

[�ص�����](#menu)

## bug ׷��

- [ ] = δ���
- [x] = �ѽ��

-----

- [ ] st-000001. �ϲ� simple_tools �е��ļ�
- [x] st-000002. �޸� simple_tools ����Ŀ¼
- [x] st-000003. ...

-----
<span id="next_version">��һ���汾</span>

[�ص�����](#menu)

## ��һ���汾��Ԥ��

- 4.1: ���� filter_ �Զ��� walls

-----
<span id="update_log">������־</span>

[�ص�����](#menu)

�ļ�������־
==========

* 4.x
    * 4.1 ����: [date_process ����](data_process.py)
        * 4.1-pre1 [2022-10-5 17:07:41]
            * ���� filter_ �е�һ�� bug
            * filter_ �Զ��� walls
            * ΢�� [maths.py](maths.py) �� saving_decomposition ����
    * 4.0 ����: [README.md ����][20221003]
        * 4.0 [2022-10-5 15:26:54]
            * �����ļ�
        * 4.0-pre3[2022-10-5 10:15:55]
            * ���� [README.md](README.md) (�ɰ汾�������ļ���[�������](README_old.md))
            * �������е� `if __name__ == '__main__':` ���Խű��� [example.py](example.py) ��
        * 4.0-pre2[2022-10-4 09:13:20]
            * merge files such as view.py, draw.py, bomb.py etc.
            * update [README.md](README.md)
            * update work space of simple_tools [%appdata%/simple_tools]
        * 4.0-pre1[2022-10-3 18:20:15]
            * rename module1 to simple_tools
            * add files named [README.md](README.md) and [LICENSE](LICENSE)
            * upload these package to [GitHub](https://gitbub.com/)
            * �� [__init__](__init__.py) �еĸ�����־ת���� [README.md](README.md)
            * simple_tools ���� Beta �汾
* 3.x
    * 3.4x
        * 3.4.6 ����: [20220925]
            * rename ~~[review.py](review.py)~~[not found] to ~~[view.py](view.py)~~[not found]
            * �� [system_extend.py](system_extend.py) ������һ����ϸ΢�� bug (��ӡ���õĿ��е� bug)
        * 3.4.5 ����: [20220925]
            * �Ż� __all__ ����, ���������ļ�
        * 3.4.4 ����: [20220918]
            * ���� [system_extend.py](system_extend.py) ��һЩ����
        * 3.4.3 ����: [20220918]
            * �� [system_extend.py](system_extend.py) �н� `from os import *` ����Ϊ `import os`
        * 3.4.2 ����: [20220918]
            * �Ż� [data_handle.py](data_process.py) �� maths.py ��������
        * 3.4.1 ����: [20220918]
            * �Ż�����ṹ[��]
        * 3.4 ����: [maths ��ѧ��������](maths.py)[20220918]
            * ���� getPrime ����
            * rename getPrime to getPrimeRange,
            * �� [2] �ָĳ� get_prime_range
            * ��� get_prime_range_of_generator ����
    * 3.3x
        * 3.3.8 ����: [from 20220901 to 20220912]
            * �Ż�����ṹ[��]
        * 3.3.7 ����: [20220825]
            * �� [default.py](default.py) �м��� clear_module1_cache ����
        * 3.3.6 ����: [20220825]
            * �Ż�����ṹ[��]
        * 3.3.5 ����: [20220824]
            * rename maths.d() to maths.is_prime()
        * 3.3.4 ����: [20220824]
            * rename [encryption.py](encr_decr.py) to [encr_decr.py](encr_decr.py)
        * 3.3.3 ����: [20220817]
            * rename get_false_unix_time to get_time_stamp
        * 3.3.2 ����: [20220817]
            * (���˸���)�� get_false_unix_time ���� 5 ��Ԥ��ֵ
        * 3.3.1 ����: [20220817]
            * �޸� [times.py](times.py) �� get_false_unix_time Ԥ��ֵ�±�Խ��� bug
        * 3.3 ����: [ʱ�亯������][20220816]
            * ������� get_false_unix_time
                * ׼���� 1,133,180,928 �ֲ�ͬ��ʱ�����ʽ, �����Լ���һ�޶���ʱ���
                * (���˸���)�Զ�����Ĭ��ʱ���ʽ
                * �޸�����һ�ѹ���� bug
    * 3.2x
        * 3.2.2 ����: [20220816]
            * ���� get_false_unix_time properties ����װ�θ�ʽ
        * 3.2.1 ����: [20220815]
            * �޸� [system_extend.py](system_extend.py) �� get_file_name ����д����־ʱ�������Ļ���ʾ��������
        * 3.2 ����: [�ļ�ϵͳ - ����Ŀ¼����][20220815]
            * ��ÿ���ļ�����������Ӧ�Ĺ���Ŀ¼
            * �洢�� [AppData/Roaming/module1](%appdata%/Roaming/module1) ��
            * ����ģ��ѭ������� ImportError
    * 3.1x
        * 3.1 ����: [system_ ����](system_extend.py)[20220815]
        * rename [system_.py](system_extend.py) Ϊ [system_extend.py](system_extend.py)
        * �� [system_extend.py](system_extend.py) ����� safe_md ����
    * 3.0x
        * 3.0.2 ����: [20220815]
            * ���� [maths.py](maths.py) �� decomposition ����
        * 3.0.1 ����: [20220814]
            * �޸� ~~[bomb.py](bomb.py)~~[not found] ��һ�� bug
        * 3.0 ����: [�ļ�ϵͳ����][20220814]
            * ӵ�����Լ��Ĺ���Ŀ¼: %APPDATA%/module1
            * �Զ����ɹ���Ŀ¼
            * ��� MODULE1_WORK_SPACE ����, ������������Ŀ¼
* 2.x
    * 2.9x
        * 2.9.1 ����: [20220814]
            * �޸� [game_disposition.py](game_disposition.py) �� Users ������� bug
        * 2.9 ����: [game_disposition ����](game_disposition.py)[20220813]
            * ���ģ���� [game_disposition.py](game_disposition.py) �е� Users ��
                * �û�
                    * �û�����
                        * �˳�ʱ���û���Ϣ�洢���ļ���
                        * ���ڵ�½ʱ��Ҫ����
                        * ���� logout �˳�����
                        * �����û����˳�ʱ�Զ���������
                * �û���ȫ
                    * topUp ��Ӧ�ú�����ܾ� temporary ��ʱ�û��ķ���
                    * __del__ ����������ܾ� self.live Ϊ False �û��ķ���
                * ��ȫ: [ʹ�ø���ȫ�� uid]
                    * ���ɷ�ʽ: ʹ�� md5 ����(ͨ���� uuid4)
                    * �ڳ������� self.info_dict['uid'] ����ʽ�洢
                    * �����û��� name ��ΪΨһ�� ID
                    * �����洢, �� name ����ȫ
                * ����
                    * ����һЩ����
                    * �Ż�ԭ���ĳ���ṹ
                    * �޸�һ�� bug
                    * ���������ļ��Ĺ���
                    * �Զ�����𻵵��ļ�
                * ̫����, ˵��������. . .
    * 2.8x
        * 2.8.4 ����: [20220813]
            * �޸� get_file_path_of_generator ���ִ�Сд����� bug
        * 2.8.3 ����: [20220812]
            * �� get_file_path_of_generator ��� case_sensitive ��������
        * 2.8.2 ����: [20220812]
            * ���� [data_handle](data_process.py) �� __all__ ����
        * 2.8.1 ����: [20220812]
            * ɾ�� ~~[review.py](review.py)~~[not found] �µ� bl_generator ����
        * 2.8 ����: [����ṹ����][20220812]
            * �½� [game_disposition.py](game_disposition.py) �ļ�
            * �� User �� �� Person �� �Ƶ� [game_disposition.py](game_disposition.py) ��
            * ɾ�� [__init__.py](__init__.py) ��һЩ���õ�����
            * ���� [__init__.py](__init__.py) ��ע��
    * 2.7x
        * 2.7.3 ����: [20220810]
            * ɾ�� [system_.py](system_extend.py) �е� get_file_name_of_generator ������
        * 2.7.2 ����: [20220810]
            * �� [hash_values.py](hash_values.py) �м��� uuid_generator ����
        * 2.7.1 ����: [20220810]
            * �� [system_.py](system_extend.py) ��, �� get_file_name_of_generator �� get_file_path_of_generator �ϲ�
        * 2.7 ����: [system_ ����](system_extend.py)[20220809]
            * ���� get_file_name
                * �������ɴ�����־�Ĺ���
                * ���� OSError ��������
            * file_pattern �����ļ�·���޷�ʶ��Ĵ�������
            * ���� get_file_path_of_generator ����, �������м��� bug
            * Ϊ get_file_path_of_generator ��� include �� exclude ��������
            * ���ģ���� File ��, ��� permission, user_id �� 10 ��������
    * 2.6x
        * 2.6.1 ����: [20220801]
            * normalEncryption �� coding ���� ���ڿ�ѡ��Ϊ `[getfilesystemencoding(), 'utf-8', 'gbk']`
        * 2.6 ����: [���ܸ���](hash_values.py)[20220801]
            * ���� md5_encryption
            * ���� normalEncryption �� bug
            * ���� normalEncryption, ���� coding ���� `['auto', 'f_byte', 'f_int']` ������ѡ��
    * 2.5x
        * 2.5.1 ����: [20220727]
            * ���� md5_encryption
            * ���� normal_encryption ����, �޸�һЩ bug
            * ���� [������־](#update_log) ������
        * 2.5 ����: [system_ ����](system_extend.py)[20220404]
        * �� [system_.py](system_extend.py) �´��� File ��
        * ��� system_pro ����������ǰ����ϵͳ
    * 2.4x
        * 2.4.4 ����: [20220320]
            * ���� [example.py](example.py) �ļ�
            * [ʱ���ж�]
        * 2.4.3 ����: [20220312]
            * ���� get_file_path_of_generator �޷����������ļ��е� bug
            * ���� file_remove, get_file_name, file_pattern
        * 2.4.2 ����: [20220305]
            * ��� random_choice ����
        * 2.4.1 ����: [20220305]
            * ɾ�� create_random ����
            * ���� file_pattern ����, ��� easy_options ����
        * 2.4 ����: [times ����](times.py)[20220305]
            * ���� [times.py](times.py) �ļ�
            * �� [times.py](times.py) �д��� get_false_unix_time ����
            * �ƶ� wait ������ [times.py](times.py) ��
            * ���� [__init__.py](__init__.py) �� __all__ ����
    * 2.3x
        * 2.3.1 ����: [20220226]
            * ���� [hash_values.py](hash_values.py) �ļ�
            * �� get_md5 �����Ƶ� [hash_values.py](hash_values.py) ��
        * 2.3 ����: [data_handle ����](data_process.py)[20220226]
            * ���²����� filter_ �� other_signs ����
            * �� [data_base.py](data_base.py) �м��� tabs Ԫ��
            * ���� __all__ ����
    * 2.2x
        * 2.2.3 ����: [20220219]
            * ���� filter_ �� other_signs ����
            * ɾ�� test() �е� draw1 ����
        * 2.2.2 ����: [20220219]
            * ���� binarySearch ����
        * 2.2.1 ����: [20220205]
            * rename username to usernameList
        * 2.2 ����: [20220205]
            * rename str_handle to data_handle
            * ɾ�� default �е� createToplevel
            * ���� ~~[test.py](test.py)~~[not found]
    * 2.1x
        * 2.1 ����: [20220203]
            * ���� file_remove �����޷�ɾ���ļ��е� bug
            * ���� file_pattern ����.
            * �� [system_.py](system_extend.py) ����� fp = getcwd() ����
            * ���� dimensionalList �� [data_handle.py](data_process.py)
    * 2.0x
        * 2.0.1 ����: [20220203]
            * ����ģ�鳣���޷����������
        * 2.0 ����: [20220203����, ��ͬ]
            * ���� file_remove, ���ģ���� system_.py
            * ���� get_file_path_of_generator �� bug
            * ���볣�� EOF = -1, NULL = None, null = 0
            * ɾ�� [__init__.py](__init__.py) �� absoluteEncryption
            * ���� [data_base.py](data_base.py) ���ݿ�.
* 1.x
    * 1.8x
        * 1.8 ����:
            * ���� [system_.py](system_extend.py)
            * �ƶ� get_file_name, get_file_name_of_generator,get_file_path, get_file_path_of_generator,
              get_file_size,get_files, get_file_names �� [system_.py](system_extend.py)
    * 1.7x
        * 1.7.1 ����:
            * ���� Users,
            * pw �� md5 ����.
        * 1.7 ����:
            * ɾ�� [__init__.py](__init__.py) �� review, digitalDecryption, draw1, draw2, breakpoint_
            * ���� breakpoint_ �� exit_ �� bug
            * ���� [randoms.py](randoms.py) ����� createRandomList
            * ɾ�� [__init__.py](__init__.py) �� passed, EuclideanAlgorithm.
    * 1.6x
        * 1.6.13 ����:
            * ���� get_file_path �� bug.
        * 1.6.12 ����:
            * �� get_file_name ���ע��.
        * 1.6.11 ����:
            * 1.���� username �ʿ�
            * 2.�޸���������� bug.
        * 1.6.10 ����:
            * 1.���� filter_ R ���ƹ��˵� bug
            * 2.�� get_files ����Ϊ get_file_path.
        * 1.6.9 ����:
            * 1.���� EuclideanAlgorithm
            * 2.ɾ�� [__init__.py](__init__.py) �� bl.
        * 1.6.8 ����:
            * 1.�� divisionAlgorithm ��������Ϊ EuclideanAlgorithm,
            * 2.ɾ�� [__init__.py](__init__.py) �� conversionSystem.
        * 1.6.7 ����:
            * �ӽ� get_file_name �� get_files ���������� default.py ��.

-----
<span id="file_history">�ļ���ʷ��¼</span>

[�ص�����](#menu)

### �������ʷ�汾(����ʱ��˳������)

1. module1_v2.5_2022_06_25_18_19_59
2. module1_v2.5.1_2022_07_27_15_32_38
3. module1_v2.7_2022_08_09_10_37_35
4. module1_v2.8.3_2022_08_13_9_11_04
5. module1_v3.0.1_2022_08_14_10_17_57
6. module1_v3.3_2022_08_16_11_00_39
7. module1_v3.3.3_2022_08_17_11_15_32
8. module1_v3.4.1_2022_09_18_11_12_29
9. module1_v3.4.5_2022_09_25_18_26_19
10. module1_v3.4.6_2022_10_03_14_21_50
11. simple_tools_v4.0-pre1_2022_10_3_18_20_15
12. simple_tools_v4.0-pre2_2022_10_4_09_47_17

-----
<span id="do_you_know">��֪����</span>

[�ص�����](#menu)

### ��֪����

