class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        ans = 0
        mx_range = -1

        for num in nums:
            x = num
            if x == 0:
                d_range = 0
            else:
                mn = 9
                mx = 0
                while x:
                    d = x%10
                    mn = min(mn,d)
                    mx = max(mx, d)
                    x //=10
                
                d_range = mx - mn

            if d_range > mx_range:
                mx_range = d_range
                ans = num
            elif d_range == mx_range:
                ans += num
        return ans
            