public class Solution {
  public int singleNumber(int[] nums) {
    Arrays.sort(nums);

    if (nums.length % 2 == 0)
    {
      return 0;
    }

    if (nums.length > 1) {
      for (int i = 0; i < nums.length - 1; i += 2) {
        if (nums[i] != nums[i + 1])
        {
          return nums[i];
        }
      }
      return nums[nums.length - 1];
    }
    return nums[0];
  }
}
