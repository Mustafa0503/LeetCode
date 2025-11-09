class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[[heights[0],0]]
        max_area = heights[0]
        old_ind=0
        for i in range(1,len(heights)):
                if(heights[i]>=stack[-1][0]):
                    stack.append([heights[i],i])

                else:
                    while(stack and heights[i]<stack[-1][0]):
                        old_ind = stack[-1][1]
                        max_area = max(max_area,(i-stack[-1][1])*stack[-1][0])
                        stack.pop()
                    stack.append([heights[i],old_ind])

        for i in stack:
            max_area = max(max_area, i[0]*(len(heights)-i[1]))
        return max_area
