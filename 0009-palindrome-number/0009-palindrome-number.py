class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        s.reverse()
        if(s[-1]=='-'):
            return False
        new_srting = ''.join(s)
        return x==int(new_srting)