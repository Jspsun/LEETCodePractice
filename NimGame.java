public class Solution {
  public boolean canWinNim(int n) {
    if ((n > 3) && (n % 4 == 0)) {
      return false;
    }

    else return true;
  }
}
