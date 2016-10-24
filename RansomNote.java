public class Solution {
  public boolean canConstruct(String ransomNote, String magazine) {
    char magazineChar[] = magazine.toCharArray();
    boolean used[]      = new boolean[magazine.length()];

    if ((magazine.length() == 0) && (ransomNote.length() != 0)) {
      return false;
    }

    for (int i = 0; i < ransomNote.length(); i++) {
      char character = ransomNote.charAt(i);

      for (int j = 0; j < magazineChar.length; j++) {
        if ((character == magazineChar[j]) && !used[j]) {
          used[j] = true;
          break;
        }
        else if (j == magazineChar.length - 1)
        {
          return false;
        }
      }
    }
    return true;
  }
}
