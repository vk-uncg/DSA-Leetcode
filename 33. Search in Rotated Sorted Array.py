class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        first = nums[0]
        if first == target:
            return 0
        for i in range(len(nums)):
            if(nums[0] != target):
                add_to_end = nums.pop(0)
                count += 1
                nums.append(add_to_end)
                print(nums[0])
            else:
                break 
        if count == len(nums):
            return -1      
        return count