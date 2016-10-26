public class Solution {
  public int[] intersection(int[] nums1, int[] nums2) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    for (int i = 0; i < nums1.length; i++) {
      if (!map.containsKey(nums1[i])) {
        map.put(nums1[i], 1);
      }
    }
    List<Integer> numbers = new ArrayList<>();

    for (int i = 0; i < nums2.length; i++) {
      if (map.containsKey(nums2[i]))
      {
        numbers.add(nums2[i]);
        map.remove(nums2[i]);
      }
    }

    // transfer array
    int newArray[] = new int[numbers.size()];

    for (int i = 0; i < numbers.size(); i++) {
      newArray[i] = numbers.get(i);
    }
    return newArray;
  }
}
