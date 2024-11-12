class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits == ""):
            return []
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
        if(len(digits)==1):
            return list(d[digits])
        s=""
        for i in digits:
            for j in d[i]:
                s=s+j
            
            let.append(s)
            s=""
        s=""
        combinations = [''.join(chars) for chars in product(*let)]
        print(combinations)
                   
                

                
        return combinations