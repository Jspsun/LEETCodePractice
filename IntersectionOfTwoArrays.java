public class Solution {
  public int[] intersection(int[] nums1, int[] nums2) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    for (int i = 0; i < nums1.length; i++) {
      if (!map.containsKey(nums1[i])) {
        map.put(nums1[i], 1);
      }
    }
    int numbers[] = new int[Math.min(nums1.length, nums2.length)];
    int counter   = 0;

    for (int i = 0; i < nums2.length; i++) {
      if (map.containsKey(nums2[i]))
      {
        numbers[counter] = nums2[i];
        map.remove(nums2[i]);
        counter++;
      }
    }

    // transfer array
    int newArray[] = new int[counter];

    for (int i = 0; i < counter; i++) {
      newArray[i] = numbers[i];
    }
    return newArray;
  }
}
