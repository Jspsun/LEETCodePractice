# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        preRev = dummy
        for i in range (m-1):
            preRev = preRev.next
        
        # reverse middle segment
        startOfRev = preRev.next
        endOfRev = preRev.next

        prev = None
        for i in range (n - m + 1):
            temp = endOfRev.next
            endOfRev.next = prev
            prev = endOfRev
            endOfRev = temp
        
        preRev.next = prev
        startOfRev.next = endOfRev
        return dummy.next
