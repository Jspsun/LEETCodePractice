# Definition for singly-linked list.
# class ListNode(object):
#
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head, None)

    def helper(self, current, prev):
        if current == None:
            return prev
        next = current.next
        current.next = prev
        return self.helper(next, current)
