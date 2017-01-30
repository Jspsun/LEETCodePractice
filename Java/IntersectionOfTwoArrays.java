public class Solution {
  public int[] intersection(int[] nums1, int[] nums2) {
    Set<Integer> temp = new HashSet<>();

    for (int i = 0; i < nums1.length; i++) {
      temp.add(nums1[i]);
    }
  }

  List<Integer> numbers = new ArrayList<>();

  for (int i = 0; i < nums2.length; i++) {
    if (temp.contains(nums2[i]))
    {
      numbers.add(nums2[i]);
      temp.remove(nums2[i]);
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
