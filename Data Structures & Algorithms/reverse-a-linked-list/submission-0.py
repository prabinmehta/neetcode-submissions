# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        next = cur
        while cur is not None:
            next = None if cur is None else cur.next
            cur.next = prev #[0,1,2,3]
            prev = cur
            cur = next
            
        head = prev
        return head
            
        