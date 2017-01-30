/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
  public int sumOfLeftLeaves(TreeNode root) {
    // terminate

    if (root == null)
    {
      return 0;
    }

    else if (root.left != null&& root.left.left == null&& root.left.right == null)
    {
      return sumOfLeftLeaves(root.right) + sumOfLeftLeaves(root.left) +
             root.left.val;
    }
    else {
      return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
    }
  }
}
