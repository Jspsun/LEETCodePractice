# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # bisect using two pointers
        rev = None
        slow = fast = head
        # reverse first half as i go
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # case to skip middle element
        if fast:
            slow = slow.next
        # cycle and exit when there is a mismatch
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        # if there was a mismatch, rev will still point to an object. Thus if
        # it points to an object the input is not a palindrome
        return not rev
