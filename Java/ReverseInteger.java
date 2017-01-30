public class Solution {
  public int reverse(int x) {
    String number = Integer.toString(x);

    if (x < 0) {
      number = number.substring(1, number.length());
    }
    String text = "";

    for (int i = number.length() - 1; i >= 0; i--) {
      text += number.charAt(i);
    }
    Long answer = Long.valueOf(text);

    if (x < 0) {
      answer *= -1;
    }

    if ((answer > Integer.MAX_VALUE) || (answer < Integer.MIN_VALUE)) {
      return 0;
    }

    int answerI = Integer.valueOf(text);

    if (x < 0) {
      answerI *= -1;
    }
    return answerI;
  }
}
