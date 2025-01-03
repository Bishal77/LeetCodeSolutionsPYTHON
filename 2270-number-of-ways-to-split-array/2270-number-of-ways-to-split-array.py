class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        n=len(nums)
        sum_left = 0
        sum_right = sum(nums)
        count = 0

        for i in range(n-1):
            #move nums[i] from right to left
            sum_left += nums[i]
            sum_right -= nums[i]

            if sum_left >= sum_right:
                count +=1
        return count

