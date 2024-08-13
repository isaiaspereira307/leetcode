# 48. Rotate Image

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                matrix[left][left + i], matrix[left + i][right], matrix[right][right - i], matrix[right - i][left] = matrix[right - i][left], matrix[left][left + i], matrix[left + i][right], matrix[right][right - i]
            left += 1
            right -= 1