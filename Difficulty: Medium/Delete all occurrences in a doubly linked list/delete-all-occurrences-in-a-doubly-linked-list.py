"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        dummy = Node(0)
        temp = head
        prev = dummy
        
        while temp:
            if temp.data != x:
                prev.next = temp
                temp.prev = prev
                prev = temp
            temp = temp.next
        
        prev.next = None
        
        return dummy.next
        