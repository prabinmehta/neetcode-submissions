# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        h3 = ListNode()
        cur = h3
        while h1 is not None and h2 is not None:
            if h1.val<h2.val:
                h4 = ListNode(h1.val)
                cur.next = h4
                cur= cur.next
                h1 = h1.next
            else:
                h4 = ListNode(h2.val)
                cur.next = h4
                cur= cur.next
                h2 = h2.next
        while h1 is not None:
            h4 = ListNode(h1.val)
            cur.next = h4
            cur= cur.next
            h1 = h1.next
        while h2 is not None:
            h4 = ListNode(h2.val)
            cur.next = h4
            cur= cur.next
            h2 = h2.next
        return h3.next

            

