# Single Number II
# deve ter espaço constante
# O(1)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for item in nums:
            ones = (ones ^ item) & ~ twos
            twos = (twos ^ item) & ~ ones
        return ones
