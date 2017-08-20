# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resList = ListNode(0)
        self.add(l1, l2, resList)
        return resList

    def add(self, n1, n2, currNode):
        if not n1 and not n2:
            return

        n1Val = 0
        n2Val = 0
        if n1:
            n1Val = n1.val
        if n2:
            n2Val - n2.val

        total = n1Val + n2Val
        currNode.val += total % 10
        currNode.next = ListNode(total / 10)
        self.add(n1.next, n2.next, currNode.next)
