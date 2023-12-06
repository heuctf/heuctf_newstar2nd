import hashlib


def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))  # 将字符串编码为字节流并更新哈希对象
    return md5_hash.hexdigest()  # 获取十六进制表示的哈希值


for i in range(1, 5000):
    md5_value = calculate_md5(str(i))
    print(re := str(i) + "的MD5哈希值:" + str(md5_value))
    with open("flag.txt", 'a+', encoding="UTF-8") as f:
        f.write(re + "\n")

