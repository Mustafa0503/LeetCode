class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = [0,0]
        has={}

        for num in range(len(nums)):
            temp = has.get(target - nums[num])
            if(temp!=None and temp!=num):
                return [temp+1, num+1 ]
            else:
                has[nums[num]]=num
        return -1