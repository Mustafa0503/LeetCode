class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        ls = []
        let = []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if(len(digits)==0):
            return []
        s=""
        combinations=[""]
        
        for i in digits:
            new_comb=[]
            word = d[i]

            for comb in combinations:
                
                for letter in word:
                   
                    new_comb.append(comb + letter)
            combinations = new_comb                   
                


                
        return combinations