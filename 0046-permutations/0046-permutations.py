class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        fin = []
        temp = []
        def rec():

            if(len(temp)==len(nums)):
                print(temp)
                fin.append(temp[:])

            for i in nums:
                if(i not in temp):
                    temp.append(i)
                    rec()
                    temp.pop()

        rec()
        return fin