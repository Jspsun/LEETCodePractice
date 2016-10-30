public class Solution {
  public String reverseString(String s) {
    StringBuilder reverse = new StringBuilder(s);

    reverse.reverse();

    return reverse.toString();
  }
}
