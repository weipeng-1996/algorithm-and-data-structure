class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while(i <= j):
            min_h = min(height[i], height[j])
            max_area = max(max_area,min_h*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area