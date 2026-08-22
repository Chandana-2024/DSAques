class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = 0
        stack = []

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                right += 1
            if right > left :
                right -= 1
            else:
                stack.append(ch)
            
        ans = ""

        while stack:
            current = stack.pop()
            if left > right  and current == "(" :
                left  -= 1
            else:
                ans += current
        
        return ans[::-1]
    