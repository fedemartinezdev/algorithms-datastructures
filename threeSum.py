def threeSumSort(nums, targetSum):
    nums.sort()
    triplets = []
    for i in range(len(nums)-2):
        L = i + 1
        R = len(nums) - 1
        while L < R:
            currentSum = nums[i] + nums[L] + nums[R]
            if currentSum == targetSum:
                triplets.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
            elif currentSum < targetSum:
                L += 1
            else:
                R -= 1
    return triplets

def threeSumUnsort(nums, target):
    tripletSeen = set()
    triplets = []
    for i, numi in enumerate(nums):
        restTarget = target - numi
        seen = set()
        for num in nums[i+1:]:
            rest = restTarget - num
            if rest in seen:
                triplet = [numi, rest, num]
                striplet = tuple(sorted([numi, rest, num]))
                if striplet not in tripletSeen:
                    triplets.append(triplet)
                    tripletSeen.add(striplet)
                continue
            
            seen.add(num)

    return list(triplets)

print(threeSumSort([-1,0,1,2,-1,-4], 0))
print(threeSumUnsort([-1,0,1,2,-1,-4], 0))