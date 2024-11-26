class Solution:
    def trap(self, height: List[int]) -> int:
        
        lef = []
        rig = [0]*len(height)
        lm = 0
        ans=0
        for i in range(len(height)):
            lef.append(lm)
            if(height[i]>lm):
                lm = height[i]
        rm = 0
        for i in range(len(height)-1,-1,-1):
            rig[i]=rm
            if(height[i]>rm):
                rm = height[i]
        for i in range(len(height)):
            temp = min(lef[i],rig[i])-height[i]
            if(temp>0):
                ans = ans + temp
        return ans
            
        

            
        

