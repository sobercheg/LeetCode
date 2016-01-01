import unittest


# -------- Internal data structures ------------
class ListNode(object):
    """ Definition for singly-linked list
    """
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

    def __eq__(self, other):
        vals_equal = self.val == other.val
        # The expression below is XOR (either is true but not both)
        only_one_next_present = bool(self.next) != bool(other.next)
        return vals_equal and not only_one_next_present

    def __repr__(self):
        return ' '.join([str(self.val), '->', str(self.next)])


# -------- Solutions --------------
class Solution(object):
    # 1. Two Sum
    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        value_to_index = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            val = nums[i]
            compl = target - val
            if compl in value_to_index and i is not value_to_index[compl]:
                return [1 + i, 1 + value_to_index[compl]]
        return []

    # 2. Add Two Numbers
    # https://leetcode.com/problems/add-two-numbers/
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def recursive(l1, l2, carryover):
            if not l1 and not l2 and not carryover:
                return

            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carryover
            if sum >= 10:
                carryover = 1
                sum -= 10
            else:
                carryover = 0

            node = ListNode(sum)
            node.next = recursive(l1, l2, carryover)
            return node

        return recursive(l1, l2, 0)


# ------- Solution unit tests ----------
class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # 1. Two Sum
    def testTwoSumStandard(self):
        # Input: numbers={2, 7, 11, 15}, target=9
        # Output: index1=1, index2=2
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2],
                         'indices of the two numbers such that they add up to the target')

        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [2, 3],
                         'indices of the two numbers such that they add up to the target')

        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [1, 4],
                         'indices of the two numbers such that they add up to the target')

    # 2. Add Two Numbers
    def testAddTwoNumbers(self):
        # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        # Output: 7 -> 0 -> 8
        self.assertEqual(self.solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))),
                                                     ListNode(5, ListNode(6, ListNode(4)))),
                         ListNode(7, ListNode(0, ListNode(8))),
                         'sum')

        # Input: (9 -> 9) + (1)
        # Output: 0 -> 0 -> 1
        self.assertEqual(self.solution.addTwoNumbers(ListNode(9, ListNode(9)),
                                                     ListNode(1)),
                         ListNode(0, ListNode(0, ListNode(1))),
                         'sum')

        # Input: (0) + (0)
        # Output: 0
        self.assertEqual(self.solution.addTwoNumbers(ListNode(0),
                                                     ListNode(0)),
                         ListNode(0),
                         'sum')


class ListNodeTest(unittest.TestCase):
    def testEq(self):
        self.assertEqual(ListNode(3), ListNode(3), 'single node equal')
        self.assertNotEqual(ListNode(3), ListNode(2), 'single node diff')
        self.assertEqual(ListNode(3, ListNode(2)), ListNode(3, ListNode(2)), 'double node equal')
        self.assertNotEqual(ListNode(3, ListNode(2)), ListNode(3), 'diff lengths')
