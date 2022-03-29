def quickSort(nums):
    return quickSortHelper(nums, 0, len(nums)-1)

def quickSortHelper(nums, leftIdx, rightIdx):
    if leftIdx >= rightIdx:
        return

    # Choose pivot 
    P = nums[(leftIdx + rightIdx) // 2]

    # Reorder and partition
    mid = partition(nums, leftIdx, rightIdx, P)
    quickSortHelper(nums, leftIdx, mid - 1)
    quickSortHelper(nums, mid, rightIdx)

def partition(nums, L, R, P):
    while L <= R:
        while nums[L] < P:
            L += 1
        while nums[R] > P:
            R -= 1
        if L <= R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
    return L

nums = [1, 1, 2, 5, 3, 0, 6, 8]
quickSort(nums)
print(nums)