class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        tup=[]
        tup=list((zip(position,speed)))
        tup.sort(reverse=True)
        for i in tup:
            if(not stack):
                stack.append(i)
            else:
                time_car = (target - i[0])/i[1]
                time_car_st = (target-stack[-1][0])/stack[-1][1]
                if(time_car>time_car_st):
                    stack.append(i)
        return len(stack)