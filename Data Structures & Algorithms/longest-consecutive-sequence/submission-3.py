class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        count = 1
        counting = 1
        for i in range(1, len(nums)):
            x = nums[i]
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                counting += 1
            else:
                counting = 1
            count = max(count, counting)
        return count           
