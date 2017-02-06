# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        return self.buildBST(head, None)

    def buildBST(self, head, tail):

        if head == tail:
            return None
        # getmiddle
        fast = head
        slow = head
        # get middle
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        Tnode = TreeNode(slow.val)
        Tnode.left = self.buildBST(head, slow)
        Tnode.right = self.buildBST(slow.next, tail)
        return Tnode
