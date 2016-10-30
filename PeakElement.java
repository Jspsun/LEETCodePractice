public class Solution {
  public int findPeakElement(int[] nums) {
    int largest = 0;

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > nums[largest]) {
        largest = i;
      }
    }
    return largest;
  }
}
