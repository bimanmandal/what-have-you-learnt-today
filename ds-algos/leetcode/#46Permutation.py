from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, p_flag):
            print(f"Inside dfs {cur} {p_flag}")
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if not p_flag[i]:
                    cur.append(nums[i])
                    p_flag[i] = True
                    dfs(cur, p_flag)
                    print(f"pop pop pop ------ {i} {nums[i]} {p_flag}")
                    p_flag[i] = False
                    cur.pop()

        dfs( [], [False] * len(nums))

        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.permute([1, 2, 3])
    print(result)
    assert result == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
