class Solution:

    def encode(self, strs: List[str]) -> str:

        result = "" # empty string first

        for s in strs:
            # add the length of the string with '#' to determine the start of the string
            result += str(len(s)) + "#" + s
        return result



    def decode(self, s: str) -> List[str]:

        result = [] # empty list first 

        i = 0 # pointer for the string

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j]) # the length in numbers is all characters between i and j 

            start = j + 1
            end = start + length

            result.append(s[start:end])

            i = end

        return result 
