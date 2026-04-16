from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = {}
        mostComm = 0
        left = 0
        maxLength = 0
        for right in range(len(s)):
                char = s[right]
                counts[char] = counts.get(char,0) +1

                mostComm = max(mostComm, counts[char])

                if right - left +1 - mostComm > k:
                        counts[s[left]] -=1
                        left +=1
                maxLength = max(maxLength, right - left +1)
        return maxLength
