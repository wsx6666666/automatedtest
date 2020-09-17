
import random

seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ天下霸唱皇天后土寒冰延华无荒古王者风范天下无双吴安华卡卡无憾无痕无悔无颜无言海涵浩瀚徜徉"
sa = []
for i in range(5):
    sa.append(random.choice(seed))
salt = ''.join(sa)
print(salt)