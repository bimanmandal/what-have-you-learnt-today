# https://leetcode.com/problems/valid-anagram/description/
"""
Approach #1
sort the characters and compare

Approach #2
use a hashmap
store the character
then compare the characters

Approach #3
take an array of 26 characters
then increment for each s and and decrement for each t

"""


class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)

        return countT == countS

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True




if __name__ == '__main__':
    solution = Solution()
    result = solution.isAnagram('anagram', 'nagaram')
    print(result)
    assert result
    result = solution.isAnagram('rat', 'car')
    print(result)
    assert not result
