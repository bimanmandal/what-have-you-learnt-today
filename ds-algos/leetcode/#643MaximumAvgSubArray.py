# https://leetcode.com/problems/maximum-average-subarray-i/description/
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum / k

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]
            max_avg = max(max_avg, cur_sum / k)

        return max_avg


if __name__ == '__main__':
    soln = Solution()
    assert soln.findMaxAverage([1, 12, -5, -6, 50, 3], k=4) == 12.75000
