public class Solution {
  public void moveZeroes(int[] nums) {
    int zeroCount = 0;

    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];

      if (num == 0) zeroCount++;

      if ((zeroCount > 0) && (num != 0)) {
        nums[i - zeroCount] = num;
        nums[i]             = 0;
      }
    }
  }
}
