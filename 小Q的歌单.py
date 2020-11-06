# Problem Description:
# 小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，
# 现在小Q想用这些歌组成一个总长度正好为K的歌单，
# 每首歌最多只能在歌单中出现一次，
# 在不考虑歌单内歌曲的先后顺序的情况下，
# 请问有多少种组成歌单的方法。

# input:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
# 接下来的一行包含四个正整数，
# 分别表示歌的第一种长度A(A<=10)和数量X(X<=100)以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。
# 保证A不等于B。
# input example:
# 5
# 2 3 3 3

# output:
# 输出一个整数,表示组成歌单的方法取模。因为答案可能会很大,输出对1000000007取模的结果。
# output example:
# 9

# Code:
import sys

def function(a,x,b,y,k):
    '求长度总和为k的不同长度歌曲的组合方案'
    sum = []
    for i in range(x+1):
        for j in range(y+1):
            if a*i+b*j == k:
                sum.append([i,j])
    return sum

def C(n,m):
    a = 1
    b = 1
    tmp_n = n
    tmp_m = m
    while tmp_n >= 1:
        a = a*tmp_m
        b = b*tmp_n
        tmp_n = tmp_n-1
        tmp_m = tmp_m-1
    return a//b

def io_main():
    s = sys.stdin.readline()
    k = int(s.strip().split()[0])
    s = sys.stdin.readline()
    a,x,b,y = int(s.strip().split()[0]),int(s.strip().split()[1]),int(s.strip().split()[2]),int(s.strip().split()[3])
    #print(k,a,x,b,y)
    result = function(a,x,b,y,k)
    if len(result)==0:
        print(0)
    else:
        total = 0
        for i in result:
            total= total + C(i[0],x)*C(i[1],y)
            total = total % 1000000007
        print(round(float(total)))

if __name__ == '__main__':
    io_main()

# 时间限制：C/C++ 1秒，其他语言2秒空间限制：C/C++ 32M，其他语言64M
# State:AC