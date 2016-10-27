public class Solution {
  public String removeDuplicateLetters(String s) {
    Set<Character> set = new HashSet<>();

    for (int i = 0; i < s.length(); i++) {
      set.add(s.charAt(i));
    }
  }
}
