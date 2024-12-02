#https://leetcode.com/problems/longest-palindromic-substring/description/
"""
Dynamic Programming 1D

Approach #1 (Brute Force)
1. Initialize `res` (longest palindrome) and `resLen` (length) as empty and 0.
2. Iterate through all substrings using two loops (`i` for start, `j` for end).
3. Use two pointers (`l` and `r`) to check if the substring is a palindrome.
4. If palindrome and longer than `resLen`, update `res` and `resLen`.
5. Return `res`.


"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = len(res)
        return res



if __name__ == '__main__':
    solution = Solution()
    result = solution.longestPalindrome("babad")
    print(result)
    assert result == "bab"
    result = solution.longestPalindrome("cbbd")
    print(result)
    assert result == "bb"