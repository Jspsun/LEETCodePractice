public class Solution {
  int sum;
  int carry;
  public int getSum(int a, int b) {
    if (b == 0) {
      return sum;
    }
    sum   = a ^ b;
    carry = (a & b) << 1;
    return getSum(sum, carry);
  }
}
