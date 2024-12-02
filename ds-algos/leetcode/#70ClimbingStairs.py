# https://leetcode.com/problems/climbing-stairs/description/
"""
Approach #1
1. Use recursion

Approach #2
1. Use recursion with memoization



"""
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def climbStairs(n):
            if memo[n] != -1: return memo[n]
            if n == 0 or n ==1 : return 1
            memo[n] = climbStairs(n - 1) + climbStairs(n - 2)
            return memo[n]
        return climbStairs(n)


if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs2(2)
    print(result)
    assert result == 2
    result = solution.climbStairs2(3)
    print(result)
    assert result == 3
