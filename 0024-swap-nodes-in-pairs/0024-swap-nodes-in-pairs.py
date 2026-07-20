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

            first  = node
            second = node.next

            remmaining = ll(second.next)

            second.next  = first
            first.next  = remmaining

            return second

        return ll(head)