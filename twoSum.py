def twoSum(nums, target):
    duplets = []
    seen = set()

    for num in nums:
        rest = target - num
        if rest in seen:
            duplets.append([rest, num])
            continue
        
        seen.add(num)
        
    return duplets

print(twoSum([-1,0,1,2,-1,-4], 0))