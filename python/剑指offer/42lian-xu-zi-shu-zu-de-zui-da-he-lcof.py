# coding=utf8
from typing import List

"""
剑指 Offer 42. 连续子数组的最大和
https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        res = nums[0]
        for i in nums:
            cur = i
            if pre > 0:
                cur += pre
            if cur > res:
                res = cur
            pre = cur
        return res


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

