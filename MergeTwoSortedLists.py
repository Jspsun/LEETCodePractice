# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newList = ListNode(0)
        cursor = newList

        while (l1 and l2):
            if (l1.val < l2.val):
                cursor.next = l1
                l1 = l1.next
            else:
                cursor.next = l2
                l2 = l2.next
            cursor = cursor.next

        cycleNode = l1
        if(cycleNode == None):
            cycleNode = l2
        cursor.next = cycleNode

        return newList.next

s = Solution()
l1 = ListNode(0)

l2 = ListNode(3)
l2.next = ListNode(4)

newList = s.mergeTwoLists(l1, l2)

while newList:
    print newList.val
    newList = newList.next
