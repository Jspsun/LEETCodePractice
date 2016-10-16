public class Solution {
  public String reverseString(String s) {
    String reverse = "";

    for (int i = s.length() - 1; i >= 0; i--)
    {
      reverse += s.charAt(i);
    }
    return reverse;
  }
}
