class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        def traverse( height:List[int]) -> int :
            left = 0 
            water = 0
            for right in range(len(height)):
                if height[left]<= height[right]:
                    index = right -left -1
                    if index > 0:
                        between = 0
                        for i in range(left + 1, right):
                            between = height[i]+between
                        level = height[left]* index - between 
                        water += level
                    left = right 
            return water
        peak = height.index(max(height))
        return traverse(height[:peak + 1]) + traverse(height[peak:][::-1])
                
            
