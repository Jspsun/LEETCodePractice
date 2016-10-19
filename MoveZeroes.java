public class Solution {
  public void moveZeroes(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 0) {
        for (int j = i + 1; j < nums.length; j++) {
          nums[j - 1] = nums[j];
        }
        nums[nums.length - 1] = 0;
      }
    }
  }
}
