class Solution:
    def printNos(self, n):
        # Code here
        def slove(n):
            if n < 1:
                return ;
            print(n, end=" ")
            slove(n-1)
            
            
        slove(n)  