/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    
    if head == nil{
        return nil
    }

    h := head
    p1 := h
    p2 := h.Next

    for p2 != nil {

        if p1.Val == p2.Val {
            p1.Next = p2.Next
            p2 = p1.Next
        }else{
            p1 = p1.Next
            p2 = p1.Next
        }
    }
    return h
}