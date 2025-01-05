def same_first_last(nums):
  if len(nums) >= 1:
    return nums[0] == nums[-1]
  else:
    return False

print(same_first_last([1, 2, 3]) )