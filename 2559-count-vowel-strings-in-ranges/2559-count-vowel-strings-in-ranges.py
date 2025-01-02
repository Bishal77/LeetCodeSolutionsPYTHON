class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowel = set("aeiou")
        prefix = [0]

        for word in words:
            is_vowel = (word[0] in vowel and word[-1] in vowel)
            if is_vowel:
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])
            
        ans = []

        for l, r in queries:
            ans.append(prefix[r+1]-prefix[l])
        return ans
            

        