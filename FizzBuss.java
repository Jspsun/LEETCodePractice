public class Solution {
  public List<String>fizzBuzz(int n) {
    List<String> output = new ArrayList<String>();

    for (int i = 1; i < n; i++)
    {
      if ((i % 5 == 0) || (i % 3 == 0))
      {
        if (i % 5 != 0)
        {
          output.add("Fizz");
        }
        else if (i % 3 != 0)
        {
          output.add("Buzz");
        }
        else
        {
          output.add("FizzBuzz");
        }
      }
      else
      {
        output.add(Integer.toString(i));
      }
    }
    return output;
  }
}
