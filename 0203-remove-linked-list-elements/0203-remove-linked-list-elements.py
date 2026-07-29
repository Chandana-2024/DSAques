# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        def ll(node):

            if  node  is None:
                return  None
            
            node.next = ll(node.next)

            if node.val == val:
                return node.next

            return node

        return ll(head)  

        