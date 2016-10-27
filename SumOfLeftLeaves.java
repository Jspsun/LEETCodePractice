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
  int counter = 0;
  public int sumOfLeftLeaves(TreeNode root) {
    // terminate

    if (root == null)
    {
      return 0;
    }

    else if (root.left != null&& root.left.left == null&& root.left.right == null)
    {
      counter += root.left.val;
    }

    sumOfLeftLeaves(root.left);
    sumOfLeftLeaves(root.right);

    return counter;
  }
}
