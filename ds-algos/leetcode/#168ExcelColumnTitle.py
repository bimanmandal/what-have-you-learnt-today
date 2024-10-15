# https://leetcode.com/problems/excel-sheet-column-title/description/
from typing import List


class Solution:
    # def convertToTitle(self, columnNumber: int) -> str:
    #     res = ""
    #     while columnNumber > 0:
    #         offset = (columnNumber - 1) % 26
    #         res += chr(ord('A') + offset)
    #         columnNumber = (columnNumber - 1 ) // 26
    #     return res[::-1]

    # Using Recursion
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0 :
            return ""
        columnNumber -= 1
        cur_chr = chr(columnNumber % 26 + ord('A'))
        return self.convertToTitle(columnNumber // 26) + cur_chr


def print_and_assert_result(expected, actual):
    print(f"actual {actual}")
    print(f"Expected {expected}")
    assert expected == actual


if __name__ == '__main__':
    solution = Solution()
    print_and_assert_result('A', solution.convertToTitle(1))
    print_and_assert_result('AB', solution.convertToTitle(28))
    print_and_assert_result('ZY', solution.convertToTitle(701))
    # print(chr(1+64))
