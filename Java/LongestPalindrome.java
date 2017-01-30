public class Solution {
  public int longestPalindrome(String s) {
    // count each occurance of a letter
    int[] letters = new int[58];

    for (int i = 0; i < s.length(); i++) {
      letters[s.charAt(i) - 'A']++;
    }

    int counter   = 0;
    boolean isOdd = false;

    for (int i = 0; i < 58; i++) {
      if (letters[i] % 2 == 0) {
        counter += letters[i];
      }
      else {
        counter += letters[i] - 1;
        isOdd    = true;
      }
    }


    if (isOdd) {
      return counter + 1;
    }

    return counter;
  }
}
