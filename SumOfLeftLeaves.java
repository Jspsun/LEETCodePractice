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
  int total;
  public int sumOfLeftLeaves(TreeNode root) {
    getTotal(root);
    return total;
  }

  public void getTotal(TreeNode root) {
    if (root.left.left == null&& root.left.right == null) {
      total += root.left.val;
    }

    if (root.left != null&& root.right != null) {
      sumOfLeftLeaves(root.left);
      sumOfLeftLeaves(root.right);
    }
  }
}
