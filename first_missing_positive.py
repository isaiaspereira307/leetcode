def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        cur = nums[i]
        if 0 < cur <= len(nums) and nums[cur -1] != cur:
            nums[i], nums[cur - 1] = nums[cur - 1], nums[i]
            continue
        i += 1

    for i in range(1, len(nums) + 1):
        if nums[i-1] != i:
            return i

    return len(nums) + 1
