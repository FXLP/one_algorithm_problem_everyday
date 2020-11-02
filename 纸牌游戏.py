# Problem Description:
# 牛牛和羊羊正在玩一个纸牌游戏。这个游戏一共有n张纸牌, 第i张纸牌上写着数字ai。
# 牛牛和羊羊轮流抽牌, 牛牛先抽, 每次抽牌他们可以从纸牌堆中任意选择一张抽出, 直到纸牌被抽完。
# 他们的得分等于他们抽到的纸牌数字总和。
# 现在假设牛牛和羊羊都采用最优策略, 请你计算出游戏结束后牛牛得分减去羊羊得分等于多少。

# 由于采用每次最优策略抽，所以进行一次排序即可按序求和
# Code:
from typing import List

def function(m_list:List[int])->int:
    m_list.sort(reverse=True)
    sum = 0
    for i in range(len(m_list)):
        sum += (-1)**i*(m_list[i])
    return sum

def io_main():
    n = int(input())
    # ints = [int(s) for s in input().split()]
    m_list = list(map(int,input().split()))
    reslut = function(m_list)
    print(reslut)

if __name__ == '__main__':
    io_main()

# Runtime:
# Memory footprint:
# 时间限制：C/C++ 1秒，其他语言2秒空间限制：C/C++ 32M，其他语言64M
# State:AC