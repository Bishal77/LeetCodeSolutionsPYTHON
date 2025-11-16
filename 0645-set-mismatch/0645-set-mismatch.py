class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0
        while i < n:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
