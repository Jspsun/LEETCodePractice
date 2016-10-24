public class Solution {
  public boolean canConstruct(String ransomNote, String magazine) {
    HashMap<Character, Integer> map = new HashMap<Character, Integer>();

    for (int i = 0; i < magazine.length(); i++) {
      if (map.containsKey(magazine.charAt(i))) {
        map.put(magazine.charAt(i), map.get(magazine.charAt(i)) + 1);
      }
      else {
        map.put(magazine.charAt(i), 1);
      }
    }

    for (int i = 0; i < ransomNote.length(); i++) {
      if (map.containsKey(ransomNote.charAt(i))) {
        map.remove(ransomNote.charAt(i));
      }
      else {
        return false;
      }
    }
    return true;
  }
}
