class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0
        current = 0
        
        for i in range(n):
            if nums[i] == 1:
                current += 1
                if current > max_count:
                    max_count = current
            else:
                current = 0
        
        return max_count
            
        
        