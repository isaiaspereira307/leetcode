# 167. Two Sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hasher = {}
        for idx, item in enumerate(nums):
            if hasher.get(item) is not None:
                return [hasher.get(item), idx]
            hasher[target-item] = idx
