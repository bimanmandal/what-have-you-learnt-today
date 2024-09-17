# Link https://leetcode.com/problems/contiguous-array/description/
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0
        diff_prefix = {}
        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
            else:
                one += 1

            if zero == one:
                res = zero + one

            diff = zero - one
            if diff in diff_prefix:
                res = max(res, i - diff_prefix[diff])
            else:
                diff_prefix[diff] = i

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMaxLength([1, 0, 1, 1]) == 2
