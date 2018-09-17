def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    t = len(nums)
    for i in range(t):
        for j in range(i+1,t):
            if nums[i] + nums[j] == target:
                return i,j
                break
            else:
                continue
