def quickSelect(nums, k):
    k = len(nums) - k
    return quickSelectHelper(nums, k, 0, len(nums)-1)

def quickSelectHelper(nums, k, leftIdx, rightIdx):
    P = nums[rightIdx]
    L = leftIdx
    for i in range(leftIdx, rightIdx):
        if nums[i] <= P:
            nums[i], nums[L] = nums[L], nums[i]
            L += 1

    nums[L], nums[rightIdx] = nums[rightIdx], nums[L]

    if L > k:
        return quickSelectHelper(nums, k, leftIdx, L - 1)
    elif L < k:
        return quickSelectHelper(nums, k, L + 1, rightIdx)
    else:
        return nums[L]

print(quickSelect([9, 1, 2, 10, 6, 5, 11], 7))