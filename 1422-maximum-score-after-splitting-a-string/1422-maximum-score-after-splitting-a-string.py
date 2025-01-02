class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones_right = [0] * (n + 1)  # Prefix sum of ones from the right

        # Calculate prefix sum of ones from the right
        for i in range(n - 1, -1, -1):
            ones_right[i] = ones_right[i + 1] + (1 if s[i] == '1' else 0)

        max_score = 0
        zeros_left = 0

        for i in range(n - 1):  # Iterate through possible split points
            zeros_left += 1 if s[i] == '0' else 0
            current_score = zeros_left + ones_right[i + 1]
            max_score = max(max_score, current_score)

        return max_score
        