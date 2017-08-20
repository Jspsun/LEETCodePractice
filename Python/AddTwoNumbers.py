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
        self.add(l1, l2, None, resList)
        return resList

    def add(self, n1, n2, prevNode, currNode):
        if not n1 and not n2 and currNode.val == 0:
            prevNode.next = None
            return

        n1Val = 0
        n2Val = 0
        if n1:
            n1Val = n1.val
            n1 = n1.next
        if n2:
            n2Val = n2.val
            n2 = n2.next

        total = n1Val + n2Val + currNode.val
        currNode.val = total % 10
        currNode.next = ListNode(total / 10)
        self.add(n1, n2, currNode, currNode.next)
