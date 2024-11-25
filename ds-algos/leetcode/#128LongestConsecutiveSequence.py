# https://leetcode.com/problems/longest-consecutive-sequence/description/


"""
Approach:
1. Convert that number list to set
2. Take only those numbers


"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == '__main__':
    solution = Solution()
    result = solution.longestConsecutive([100, 4, 200, 1, 3, 2])
    print(result)
    assert result == 4
    result = solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(result)
    assert result == 9
