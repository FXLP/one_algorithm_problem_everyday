# Problem Description:
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

# Code:
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and (n + self.Sum_Solution(n-1))

s = Solution()
sum = s.Sum_Solution(10)
print(sum)

# Runtime:18ms
# Memory footprint:5748KB
# State:Accept