# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None: return None

        h = head 
        p = h
        p2 = h.next

        while p2 :
            if p.val == p2.val:
                p.next = p2.next
                p2 = p.next 
            else:
                p = p.next
                p2 = p.next

        return h
