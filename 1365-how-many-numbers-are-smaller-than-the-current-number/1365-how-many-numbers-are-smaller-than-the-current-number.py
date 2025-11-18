class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        
        # Count occurrences
        for x in nums:
            freq[x] += 1
        
        # Prefix sum: freq[i] = count of numbers < i
        for i in range(1, 101):
            freq[i] += freq[i - 1]
        
        
        return [0 if x == 0 else freq[x - 1] for x in nums]
