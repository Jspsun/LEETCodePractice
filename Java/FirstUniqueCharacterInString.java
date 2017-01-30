public class Solution {
  public int firstUniqChar(String s) {
    Set<Character> set        = new HashSet<>();
    Set<Character> setRepeats = new HashSet<>();

    for (int i = 0; i < s.length(); i++) {
      if (set.contains(s.charAt(i))) {
        setRepeats.add(s.charAt(i));
      }
      set.add(s.charAt(i));
    }

    for (int i = 0; i < s.length(); i++) {
      if (!setRepeats.contains(s.charAt(i))) {
        return i;
      }
    }
    return -1;
  }
}
