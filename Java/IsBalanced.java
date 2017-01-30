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
  public boolean isBalanced(TreeNode root) {
    if (root == null) {
      return true;
    }

    if ((Math.abs(getDepth(root.left) - getDepth(root.right)) > 1) ||
        (isBalanced(root.left) == false) ||
        (isBalanced(root.right) == false)) {
      return false;
    }
    return true;
  }

  public int getDepth(TreeNode root) {
    if (root == null) {
      return 0;
    }
    return 1 + Math.max(getDepth(root.left), getDepth(root.right));
  }
}
