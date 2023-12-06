import os


flag = ""
t0 = 1699056000
for i in range(0, 26):
    char = str(chr(int(os.path.getmtime(str(i) + ".txt") - t0)))
    print(str(i) + ".txt对应字母:" + char)
    flag += str(char)
print(flag)

