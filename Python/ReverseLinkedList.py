# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        next = head
        prev = None

        while next != None:
            current = next
            next = next.next
            current.next = prev
            prev = current
        return prev
