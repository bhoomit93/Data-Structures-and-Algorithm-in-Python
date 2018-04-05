"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""

        for i, values in enumerate(values):
            result = result + (num // values) * numerals[i]
            num = num % values

        return result


def main():
    nums = [1, -3, 0, -5, 3, 5, 6, 7]
    n = len(nums)

    test = 3100

    S = Solution()
    print(S.intToRoman(test))


if __name__ == '__main__':
    main()
