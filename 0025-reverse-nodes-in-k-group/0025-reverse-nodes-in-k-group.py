# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, start, end):
        prev , curr  =  None ,start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt , temp = 0,head

        while temp and cnt < k:
            temp = temp.next
            cnt +=1
        if cnt < k :
            return head
        
        new_head = self.reverse(head,temp)
        head.next = self.reverseKGroup(temp, k)
        return new_head
        