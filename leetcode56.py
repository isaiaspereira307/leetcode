# 56. Merge Intervals

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start > last_end:
                merged.append([start, end])
            else:
                merged[-1][1] = max(last_end, end)
        return merged