# 42. Trapping Rain Water

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        water = [0]*n
        high = 0
        for i in range(0, n):
            if height[i] > high:
                high = height[i]
            if height[i] < high:
                water[i] += high - height[i]
        high = 0
        for i in range(n-1, 0, -1):
            if height[i] > high:
                high = height[i]
            diff = high - height[i]
            if diff < water[i]:
                water[i] = diff
        return sum(water)