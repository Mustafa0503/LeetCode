class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_board = {
            1: [],                2: ['a', 'b','c'],    3: ['d','e','f'],
            4: ['g','h','i'],     5: ['j','k','l'],     6: ['m','n','o'],
            7: ['p','q','r','s'], 8: ['t','u','v'],     9: ['w','x','y','z']
        }

        ans = []
        temp = []
        letters = []
        for i in digits:
            letters.append(phone_board.get(int(i)))
        print(letters)
        def dfs(ind):
            if len(temp)==len(digits):
                ans.append("".join(temp.copy()))
                return
            for i in letters[ind]:
                temp.append(i)
                dfs(ind+1)
                temp.pop()
        dfs(0)
        return ans