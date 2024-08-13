# 15. 3sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for idx, item in enumerate(nums):
            if idx > 0 and item == nums[idx-1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                three_sum = item + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([item, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result