import unittest

class Solution(object):

    # 1. Two Sum: https://leetcode.com/problems/two-sum/
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        valueToIndex = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            val = nums[i]
            compl = target - val
            if compl in valueToIndex and i is not valueToIndex[compl]:
                return [1 + i, 1 + valueToIndex[compl]]
        return []


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSumStandard(self):
        # Input: numbers={2, 7, 11, 15}, target=9
        # Output: index1=1, index2=2
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2],
                         'indices of the two numbers such that they add up to the target')

        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [2, 3],
                         'indices of the two numbers such that they add up to the target')

        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [1, 4],
                         'indices of the two numbers such that they add up to the target')
