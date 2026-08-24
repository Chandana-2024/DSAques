class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for ch in  s:
            if  ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        st = []
        for ch in t:
            if ch == "#":
                if st:
                    st.pop()
            else:
                st.append(ch)

        if  stack == st:
            return True
        
        return False

        

        
        

        