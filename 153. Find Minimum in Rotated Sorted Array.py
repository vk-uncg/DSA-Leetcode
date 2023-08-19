class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = int((low + high) / 2)

        while(mid < high):
            if(nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid
            mid = int((low + high) / 2)
        
        return nums[low]
    