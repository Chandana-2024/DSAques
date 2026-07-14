class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        cad = 0

        for num in nums:
            if  cnt == 0:
                cad = num
            if cad == num:
                cnt +=1
            else:
                cnt -=1
        
        return cad

        