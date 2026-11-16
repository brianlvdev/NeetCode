class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefixo = 1
        for i in range(n):
            res[i] = prefixo
            prefixo *= nums[i]
        sufixo = 1
        for i in range(n - 1, -1, -1):
            res[i] *= sufixo
            sufixo *= nums[i]
            
        return res
