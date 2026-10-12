class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        target =0
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1 , len(nums)):
                needed = target -nums[i] - nums[j]
                if needed in seen:
                    temp = sorted([nums[i], nums[j] , needed])
                    if temp not in result:
                        result.append(temp)
            
                seen.add(nums[j])
        return result