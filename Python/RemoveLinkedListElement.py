# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # shift while head ==val
        while head != None and head.val == val:
            head = head.next

        if head == None:
            return head
        prev = head
        temp = head.next
        while temp != None:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head
