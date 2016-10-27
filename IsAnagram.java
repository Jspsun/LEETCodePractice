public class Solution {
  public boolean isAnagram(String s, String t) {
    int[] sChars = new int[26];
    int[] tChars = new int[26];

    if (s.length() != t.length()) {
      return false;
    }

    for (int i = 0; i < s.length(); i++) {
      sChars[s.charAt(i) - 'a']++;
      tChars[t.charAt(i) - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
      if (sChars[i] != tChars[i]) {
        return false;
      }
    }
    return true;
  }
}
