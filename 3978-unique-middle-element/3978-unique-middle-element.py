class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        target = nums[n//2]
        cnt = 0
        for i in range(n):
            if  nums[i] == target:
                cnt += 1
                if cnt > 1:
                    return False

        return True