def insert(root,node):
    if not root:
        root = node
    else:
        if node.val > root.val:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)