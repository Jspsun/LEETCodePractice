public class Solution {
  public int majorityElement(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      if (map.containsKey(nums[i])) {
        map.put(nums[i], map.get(nums[i]) + 1);
      }
      else {
        map.put(nums[i], 1);
      }
    }
    int largestVal = 0;
    int largestKey = 0;

    for (int currentInt:map.keySet()) {
      if (map.get(currentInt) > largestVal) {
        largestKey = currentInt;
        largestVal = map.get(largestKey);
      }
    }
    return largestKey;
  }
}
