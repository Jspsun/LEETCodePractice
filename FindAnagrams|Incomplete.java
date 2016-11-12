public class Solution {
  public List<Integer>findAnagrams(String s, String p) {
    Map map < Character, Integer >= new Hashmap<>();

    List list < Integer >= new ArrayList<>();

    // load up hashmap
    for (int i = 0; i < p.length(); i++) {
      if (map.contains(p.charAt(i))) {
        map.setValue(p.charAt(i), map.get(p.charAt(i) + 1));
      }
      else {
        map.setValue(p.charAt(i), 1);
      }
    }

    for (int i = 0; i < s.length() - p.length(); i++) {
      String temp = s.substring(i, i + p.length);

      Map local < Character, Integer >= new Hashmap<>();

      for (int j = 0; j < temp.length; j++) {
        if (local.contains(temp.charAt(j))) {
          local.setValue(temp.charAt(j), local.get(temp.charAt(j) + 1));
        }
        else {
          local.setValue(temp.charAt(i), 1);
        }
      }

      if (local.equals(map)) {
        list.add(i);
      }
    }

    // list to Array
    int array[] = new int[list.size()];

    for (int i = 0; i < list.size(); i++) {
      array[i] = list.get(i);
    }
  }
}
}
