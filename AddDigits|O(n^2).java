public class Solution {
  public int addDigits(int num) {
    if (num <= 9) {
      return num;
    }
    String numberS = Integer.toString(num);
    int    number  = 0;

    for (int i = 0; i < numberS.length(); i++) {
      number += numberS.charAt(i) - '0';
    }
    return addDigits(number);
  }
}
