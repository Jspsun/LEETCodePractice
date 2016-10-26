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
  static HashMap<TreeNode, TreeNode> map = new HashMap<>();

  static Set<TreeNode> set = new HashSet<>();
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    setUp(root);
    setUpSet(p);


    while (q != null) {
      if (set.contains(q)) {
        return q;
      }
      q = getParent(q);
    }
    return null;
  }

  public void setUp(TreeNode root) {
    if (root == null) {
      return;
    }

    map.put(root.left,  root);
    map.put(root.right, root);

    setUp(root.left);
    setUp(root.right);
  }

  public void setUpSet(TreeNode root) {
    while (root != null) {
      set.add(root);
      root = getParent(root);
    }
  }

  public TreeNode getParent(TreeNode root) {
    return map.get(root);
  }
}
