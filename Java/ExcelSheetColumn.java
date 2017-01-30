public class Solution {
  public int titleToNumber(String s) {
    int counter = 0;

    for (int i = s.length() - 1; i >= 0; i--) {
      counter += Math.pow(26, s.length() - i - 1) * (s.charAt(i) - 'A' + 1);
    }
    return counter;
  }
}
