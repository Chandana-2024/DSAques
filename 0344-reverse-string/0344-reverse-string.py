class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def slove(l,r):
            if l >= r:
                return True
            
            s[l],s[r] = s[r],s[l]

            return slove(l+1,r-1)
        n=len(s)
        slove(0,n-1)
        