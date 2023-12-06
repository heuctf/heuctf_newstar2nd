import os
import time
import sys
from pywintypes import Time  # 可以忽视这个报错，不会影响程序的运行
from win32con import FILE_FLAG_BACKUP_SEMANTICS
from win32con import FILE_SHARE_WRITE
from win32file import CloseHandle
from win32file import CreateFile
from win32file import GENERIC_WRITE
from win32file import OPEN_EXISTING
from win32file import SetFileTime


def modify_file_create_time(file_name, create_time_str, update_time_str, access_time_str):
    try:
        format_str = "%Y-%m-%d %H:%M:%S"  # 时间格式
        f = CreateFile(filename, GENERIC_WRITE, 0, None, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS, 0)
        create_time = Time(time.mktime(time.strptime(create_time_str, format_str)))
        update_time = Time(time.mktime(time.strptime(create_time_str, format_str)))
        access_time = Time(time.mktime(time.strptime(create_time_str, format_str)))
        SetFileTime(f, create_time, update_time, access_time)
        CloseHandle(f)
        print('update file time success:{}/{}/{}'.format(create_time_str, update_time_str, access_time_str))
    except Exception as e:
        print('update file time fail:{}'.format(e))


def create_file(file_name):
    try:
        with open(filename, 'w') as f:
            pass
    except Exception as e:
        print(e)
        sys.exit()


flag = 'orgctf{we1c0me_to_jOin_us}'
flag_list = []
for i in flag:
    flag_list.append(ord(i))
print(flag_list)
test_time = 1699056000
for i in range(len(flag_list)):
    filename = str(i) + '.txt'
    create_file(filename)
    change_time = time.localtime(test_time + flag_list[i])
    up_time = time.strftime("%Y-%m-%d %H:%M:%S", change_time)
    modify_file_create_time(filename, up_time, up_time, up_time)

# filename = '0.txt'
# file_ctime = os.stat(filename).st_ctime
# print(file_ctime)
