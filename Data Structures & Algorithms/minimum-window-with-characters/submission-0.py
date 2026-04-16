class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
        
        target_counts = {}
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1
        
        required = len(target_counts)
        window_counts = {}
        formed = 0

        # (length, left, right)
        ans = (float('inf'), None, None)

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Contract the window
            while left <= right and formed == required:
                char_left = s[left]
                
                # Update the result if this window is smaller
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Process the character being removed from the left
                window_counts[char_left] -= 1 # FIXED: Used char_left instead of char
                if char_left in target_counts and window_counts[char_left] < target_counts[char_left]:
                    formed -= 1
                
                left += 1
                
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]