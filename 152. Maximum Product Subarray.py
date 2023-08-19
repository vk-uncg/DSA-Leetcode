class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_prod = 1
        max_prod = -9999

        for i in range(len(nums)):
            #current_prod = max(current_prod*nums[i], nums[i])
            current_prod = current_prod*nums[i]
            max_prod = max(current_prod, max_prod)
            if(current_prod == 0):
                current_prod = 1
        current_prod = 1
        for i in range(len(nums)-1, -1, -1):
            current_prod = current_prod*nums[i]
            max_prod = max(current_prod, max_prod)
            if(current_prod == 0):
                current_prod = 1
        return max_prod