"""
import random
list = []
for i in range(6):
    a = random.randint(1, 34)
    list.append(a)
b = random.randint(1,17)
list.append(b)
print(list)
"""
def quchong(filepath):
    pl = [filepath]
    l1 = []
    l2 = []
    for path in pl:
        with open(path,"r") as f:
            # 打开初始密码文件
            for a in f.readlines():
                a = a.strip('\n')
                if len(a) > 8 or len(a) == 8:
                    # 取长度大于8位的字符串
                    l1.append(a)
        f.close()
        # 关闭文件
    for i in l1:
        if i not in l2:
            # 去重
            l2.append(i)
    for p in l2:
        with open("D:\\下载\\new_passwords.txt", "a") as w:
            # 追加写入新的文件
            w.writelines(p+"\n")
    w.close()
if __name__ == '__main__':
    quchong("D:\\下载\\birthday.txt")