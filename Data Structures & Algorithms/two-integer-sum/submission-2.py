class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in   enumerate(nums):
            rem = target - num 
            if rem in nums[i+1:]: 
                return [ i , nums.index(rem , i+1)]
