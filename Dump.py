import os,platform
os.system('git pull')
os.system('clear')
print(' SXB Tools Loading')
xd=platform.architecture()[0]
if xd=="32bit":
    print('[+] \33[1;32mTHIS IS ONLY 64 BIT')
if xd=="64bit":
    __import__("Dump")
