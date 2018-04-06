"""

@author: Bhoomit Patel

"""
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums, n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()

        # 1 - Sorting the array
        list.sort(nums)

        for i in range(0, n - 1):
            l = i + 1
            r = n - 1
            while (l < r):

                if (nums[i] + nums[l] + nums[r] == 0):
                    result.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                elif (nums[i] + nums[l] + nums[r] < 0):
                    l += 1

                else:
                    r -= 1

        print(result)


def main():
    nums = [1, -3, 0, -5, 3, 5, 6, 7]
    n = len(nums)
    S = Solution()
    S.threeSum(nums=nums, n=n)


if __name__ == '__main__':
    main()
