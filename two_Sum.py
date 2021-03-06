"""

@author: Bhoomit Patel

"""
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:



    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

        d = dict()

        for i in range(len(nums)):
            key = target - nums[i]
            if key in d:
                return [d[key], i]
            else:
                d[nums[i]] = i

        return []


def main():
    nums = [1, 3, 5, 6, 7]
    target = 12
    S = Solution()
    print(S.twoSum(nums=nums,target=target))


if __name__ == '__main__':
    main()
