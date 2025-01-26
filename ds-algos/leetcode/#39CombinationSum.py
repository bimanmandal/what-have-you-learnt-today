from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i  >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res



if __name__ == '__main__':
    solution = Solution()
    result = solution.combinationSum([2,3,6,7], 7)
    assert result ==[[2,2,3],[7]]