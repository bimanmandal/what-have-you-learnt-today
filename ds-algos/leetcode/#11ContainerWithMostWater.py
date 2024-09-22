# https://leetcode.com/problems/container-with-most-water/description/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
    assert result == 49
