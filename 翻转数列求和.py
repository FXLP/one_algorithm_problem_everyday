# Problem Description:
# 小Q定义了一种数列称为翻转数列:
# 给定整数n和m, 满足n能被2m整除。对于一串连续递增整数数列1, 2, 3, 4..., 每隔m个符号翻转一次, 最初符号为'-';。
# 例如n = 8, m = 2, 数列就是: -1, -2, +3, +4, -5, -6, +7, +8.
# 而n = 4, m = 1, 数列就是: -1, +2, -3, + 4.
# 小Q现在希望你能帮他算算前n项和为多少。

# Code:
import sys
 
while True:
    try:
        s = sys.stdin.readline()
        n,m = int(s.strip().split()[0]),int(s.strip().split()[1])
        print(m*n/2)
    except:
        break

# Runtime:
# Memory footprint:
# 时间限制：C/C++ 1秒，其他语言2秒空间限制：C/C++ 32M，其他语言64M
# State:AC