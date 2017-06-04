# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        POdd = head
        PEven = head.next
        PEvenHead = PEven

        while PEven and PEven.next:
            POdd.next = POdd.next.next
            PEven.next = PEven.next.next
            POdd = POdd.next
            PEven = PEven.next
        POdd.next = PEvenHead
        return head

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
h.next.next.next.next.next = ListNode(6)
h.next.next.next.next.next.next = ListNode(7)
h.next.next.next.next.next.next.next = ListNode(8)

n = Solution().oddEvenList(h)
while n:
    print n.val
    n = n.next
