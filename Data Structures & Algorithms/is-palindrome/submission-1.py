class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        So first we read the first word of the String
        then we keep track of all the letters of that word 
        then we have to reverse the letter and the last letter we check whether it's upper or lower case

        return true if the pattern is reversed correctly with case sensitivity
        return false if not

        Can we keep track of spaces between words to find out when the first word is done and when the last word starts?

        Am I overthinking this?

        Should we turn the letters to numbers using ASCII chars and then figure out the order that way? 
        How would we start though? 

        '''
        

        # actual solution 
        # We filter out everything except the String, and make it all lowercase
        # Then we check to see if the filtered String is the same as its reverse

        # use .lower() and .isalnum()

        left, right = 0, len(s) - 1

        # while left < right:

        #     if not s[left].isalnum():
        #         left += 1 # keep going if it's not a alphanumeric
        #     elif not s[right].isalnum():
        #         right -= 1
        #     else:
                
        #         if s[left].lower() != s[right].lower():

        #             return False # if characters don't match then return false

        #         # move closer to the center throughout the loop 
        #         left += 1
        #         right -= 1 
            
        # return True


        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


