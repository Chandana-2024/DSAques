class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def slove(left , right):
            if left >= right :
                return  True 
            
            s[left] , s[right] = s[right] , s[left]
            slove(left+1,right-1)

        n = len(s) -1
        slove(0,n)
        


        