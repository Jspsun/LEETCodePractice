/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
  public ListNode removeElements(ListNode head, int val) {
    ListNode temp = head;

// Method 1: null pointers
while (temp != null) {
  if (temp.val == val) {
    temp.val  = temp.next.val;
    temp.next = temp.next.next;
  }
  temp = temp.next;
} return head;



  // while ((temp != null) && (temp.next != null)) {

//   if (temp.next.val == val)
//   {
//     temp.next = temp.next.next;
//   }
//
//   if ((temp.next.next != null)) {
//     temp = temp.next;
//   }
// }
// return head;

  }
}
