def helper(root, diameter):
    if not root:
        return 0
    left = helper(root.left, diameter)
    right = helper(root.right, diameter)
    if left + right > diameter[0]:
        diameter[0] = left + right
    return max(left, right) + 1

# main function


def getDiameterTree(root):
    answer = [0]
    helper(root, answer)
    return answer[0]


from TestObjects import BinaryTree
b = BinaryTree()
print getDiameterTree(b.root)
