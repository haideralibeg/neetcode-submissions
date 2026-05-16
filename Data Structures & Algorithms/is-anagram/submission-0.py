class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if the characters of s = the characters of t then return true 
        # else return false
        # now I need to put this in logic... 
        # the length and the characters of the strings have to be the same 
        # 

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

        # if sorted(s) == sorted(t):
        #     return True
        # else: 
        #     return False

        


