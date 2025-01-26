from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(start, combine):
            if len(combine) == k:
                res.append(combine.copy())
                return
            for i in range(start, n + 1):
                combine.append(i)
                dfs(i + 1, combine)
                combine.pop()
        dfs(1, [])
        return res




if __name__ == '__main__':
    solution = Solution()
    result = solution.combine(4, 2)
    print(result)
    assert result == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
