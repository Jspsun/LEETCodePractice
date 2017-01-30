public class Solution {
  public char findTheDifference(String s, String t) {
    int STotal = 0;
    int TTotal = 0;

    for (int i = 0; i < s.length(); i++) {
      STotal += s.charAt(i);
      TTotal += t.charAt(i);
    }
    TTotal += t.charAt(t.length() - 1);

    return (char)(TTotal - STotal);
  }
}
