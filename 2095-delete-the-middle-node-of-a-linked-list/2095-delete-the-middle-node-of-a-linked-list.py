# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  not head or not head.next:
            return None
        
        slow  = head
        fast = head
        temp  = None

        while fast != None and fast.next != None:
            temp = slow
            fast = fast.next.next
            slow = slow.next

        temp.next = slow.next
        del slow

        return head
    
