public class Solution {
  public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
    int iterations = (int)(Math.floor(minutesToTest / minutesToDie));

    return (int)(Math.round(Math.log(buckets) / Math.log(iterations)));
  }
}
