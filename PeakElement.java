public class Solution {
  public int findPeakElement(int[] nums) {
    int[] extended = new int[nums.length + 2];
    extended[0]                   = Integer.MIN_VALUE;
    extended[extended.length - 1] = Integer.MIN_VALUE;

    for (int i = 0; i < nums.length; i++) {
      extended[i + 1] = nums[i];
    }

    for (int i = 1; i < extended.length - 1; i++) {
      if ((extended[i] > extended[i - 1]) && (extended[i] > extended[i + 1])) {
        return i - 1;
      }
    }
    return 0;
  }
}
