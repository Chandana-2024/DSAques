# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def ll(node):
            if node is None or node.next is None:
                return node
            
            new_head = ll(node.next)

            node.next.next = node
            node.next = None

            return new_head

        return ll(head) 




        


