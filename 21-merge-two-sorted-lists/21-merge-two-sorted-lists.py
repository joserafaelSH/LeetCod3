# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0 ,next=None):
        self.val = val
        self.next = next
        
            
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       

        current1, current2 = list1, list2

        if current1 is None:
            return list2
        elif current2 is None:
            return list1
        
        final_node = None
        current_node = None
        if current1.val < current2.val:
            final_node = current1
            current_node = current1
            current1 = current1.next
        else:
            final_node = current2
            current_node = current2
            current2 = current2.next

        while current1 and current2:
            if current1.val < current2.val:
                current_node.next = current1
                current1 = current1.next
            else:
                current_node.next = current2
                current2 = current2.next
            
            current_node = current_node.next
        

        current_node.next = current1 if current1 else current2

        return final_node
            