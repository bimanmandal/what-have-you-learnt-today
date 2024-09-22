# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i <= j:
            curSum  = numbers[i] + numbers[j]
            if curSum == target: return [i + 1, j + 1]
            if curSum > target:
                j -= 1
            else:
                i += 1
        return []


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
