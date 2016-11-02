public class Solution {
  public String addStrings(String num1, String num2) {
    int[] number = new int[Math.max(num1.length(), num2.length()) + 1];

    int num1Index = num1.length() - 1;
    int num2Index = num2.length() - 1;

    for (int i = number.length - 2; i > 0; i--) {
      if (num1Index >= 0) {
        number[i] += num1.charAt(num1Index) - '0';
        num1Index--;
      }

      if (num2Index >= 0) {
        number[i] += num2.charAt(num2Index) - '0';
        num2Index--;
      }

      // carry over first digit if >9

      if (number[i] > 9) {
        number[i - 1] += number[i] / 10;
        number[i]      = number[i] % 10;
      }
    }

    // turn number into string
    String s = "";

    for (int i = 0; i < number.length; i++) {
      s += Integer.toString(number[i]);
    }

    if (s.charAt(0) == '0')

    {
      s = s.substring(1);
    }

    return s;
  }
}
