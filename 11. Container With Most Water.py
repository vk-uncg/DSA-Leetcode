class Solution:
    def maxArea(self, height: List[int]) -> int:
        current_area = 0
        max_area = 0
        left = 0
        right = len(height) - 1

        while(left < right):
            current_area = (right - left) * min(height[right], height[left])
            max_area = max(max_area, current_area)

            if(height[left] >= height[right] + 1):
                right = right - 1
            elif(height[right] >= height[left] + 1):
                left = left + 1
            else:
                left = left + 1
                right = right - 1

        return max_area