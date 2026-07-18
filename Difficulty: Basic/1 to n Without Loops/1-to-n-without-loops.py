class Solution:
    def printTillN(self, n):

        def solve(i):
            if i > n:
                return

            print(i, end=" ")
            solve(i + 1)

        solve(1)