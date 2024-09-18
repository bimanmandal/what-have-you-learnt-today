# https://leetcode.com/problems/subarray-sum-equals-k/description/
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        res = 0
        curSum = 0
        for n in nums:
            curSum += n
            diff =  curSum -k
            res += prefix_sum.get(diff, 0)
            prefix_sum[curSum] = 1 + prefix_sum.get(curSum, 0)

        return res



if __name__ == '__main__':
    soln = Solution()
    assert soln.subarraySum([1,2,3], 3) == 2