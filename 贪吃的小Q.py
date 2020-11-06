# Problem Description:
# 小Q的父母要出差N天，走之前给小Q留下了M块巧克力。
# 小Q决定每天吃的巧克力数量不少于前一天吃的一半，
# 但是他又不想在父母回来之前的某一天没有巧克力吃，
# 请问他第一天最多能吃多少块巧克力？

# input:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含两个正整数，表示父母出差的天数N(N<=50000)和巧克力的数量M(N<=M<=100000)。
# input example:3 7

# output:
# 输出一个数表示小Q第一天最多能吃多少块巧克力。
# output example:4

# Code:
from typing import List
import sys

def function(num,n):
    '计算第一天吃num块时n天至少吃的总数量'
    sum = 0
    for i in range(0,n):
        sum += num
        num = (num+1)//2
    return sum

def BinarySearch(n,m):
    if n == 1:
        return m
    low = 1
    high = m
    while low<high:
        mid = (low+high+1)//2
        if function(mid,n)<=m:
            low = mid
        else:
            high = mid-1
    return low

def io_main():
    s = sys.stdin.readline()
    n,m = int(s.strip().split()[0]),int(s.strip().split()[1])
    #print(n,m)
    reslut = BinarySearch(n,m)
    print(reslut)

if __name__ == '__main__':
    io_main()

# 时间限制：C/C++ 1秒，其他语言2秒空间限制：C/C++ 32M，其他语言64M
# State:AC