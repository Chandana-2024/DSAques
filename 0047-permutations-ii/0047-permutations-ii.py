class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []

        def getperms(idx):
            
            if idx == n:
                ans.append(nums[:])
                return

            used = set()
            
            for i in range(idx,n):
                if  nums[i] in used:
                    continue

                used.add(nums[i])
                nums[i],nums[idx] = nums[idx],nums[i]
                getperms(idx+1)
                nums[i],nums[idx] = nums[idx],nums[i]
        
        getperms(0)
        return ans
        