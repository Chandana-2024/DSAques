class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if  n >0:
            if n == 1:
                return x

            if n %2 == 0:
                a = self.myPow(x,n//2)
                return a*a
            else:
                a = self.myPow(x,n//2)
                return a*a*x
        elif n == 0:
            return 1
        else:
            return self.myPow(1/x,-n)
