public class Solution {
  public List<Integer>majorityElement(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      if (map.containsKey(nums[i])) {
        map.put(nums[i], map.get(nums[i]) + 1);
      }
      else {
        map.put(nums[i], 1);
      }
    }
    int majority       = nums.length / 3;
    List<Integer> list = new ArrayList<Integer>();

    for (int currentInt:map.keySet()) {
      if (map.get(currentInt) > majority) {
        list.add(currentInt);
      }
    }
    return list;
  }
}
