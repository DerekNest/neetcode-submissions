class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 1
        nums.sort()
        currentLongest = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i]  == nums[i-1]+1:
                currentLongest +=1
            else:
                longest = max(longest,currentLongest)
                currentLongest=1
        return max(longest, currentLongest)
