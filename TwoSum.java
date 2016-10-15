public class Solution {
  public int[] twoSum(int[] nums, int target) {
    int[] numbers = new int[2];

    for (int i = 0; i < nums.length; i++)
    {
      numbers[0] = i;
      int difference = target - nums[i];

      for (int j = i + 1; j < nums.length; j++)
      {
        if (nums[j] == difference)
        {
          numbers[1] = j;

          // asda
          return numbers;
        }
      }
    }
    return numbers;
  }
}
