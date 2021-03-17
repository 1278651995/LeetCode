# coding=utf8

"""
剑指 Offer 39. 数组中出现次数超过一半的数字
https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
思路： 摩尔投票
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1

        count = 0
        for num in nums:
            if num == x:
                count += 1

        return x if count > len(nums) // 2 else 0


if __name__ == '__main__':
    print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))