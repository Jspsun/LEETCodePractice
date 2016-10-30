public class Solution {
  public int myAtoi(String str) {
    int number       = 0;
    int counter      = 0;
    boolean negative = false;

    for (int i = 0; i < str.length(); i++) {
      if (!Character.isDigit(str.charAt(i))) {
        if (str.charAt(i) == '-') {
          negative = true;
        }

        String temp =
          str.substring(0, i) + str.substring(i + 1, str.length());
        str = temp;
      }
    }

    for (int i = (str.length() - 1); i >= 0; i--) {
      number += Math.pow(10, counter) * (str.charAt(i) - '0');
      counter++;
    }

    if (negative) {
      number *= -1;
    }
    return number;
  }
}
