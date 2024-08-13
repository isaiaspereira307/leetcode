# Prefix-Sum
# 303. Range Sum Query-Immutable
# tempo O(1)
# Espaço O(n)

class Solution:
    def __init__(self, nums: list[int]):
        self._sum = []
        total = 0
        for item in nums:
            total += item
            self._sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self._sum[right] - self._sum[left-1]
        else:
            return self._sum[left or right]
