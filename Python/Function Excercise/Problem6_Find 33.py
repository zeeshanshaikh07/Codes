def has_33(nums):
    result = ""
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
result = has_33([1,3,1,3])
print(result)