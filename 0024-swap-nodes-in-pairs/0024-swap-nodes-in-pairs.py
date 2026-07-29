# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def ll(node):

            if node is None or node.next is None:
                return node

            first = node
            secound = node.next

            rem = ll(secound.next)

            secound.next = first
            first.next = rem

            return secound
            
        return ll(head)