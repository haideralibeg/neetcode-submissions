class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # With a String we need to find a sequence of continuous characters
        # In the String keep track of all the characters
        # if the chracters are the same without duplicates then add it to the sequence

        # a variable sequence

        # so a left pointer that starts at the first character
        # a right that is right after the left
        # then move the left after the right and right after the left
        # with a variable that can hold a temp_sequence
        # keeping track of all the charcters and if they are repeating
        # if the characters are all different then record the sequence?
        # if we get a single duplicate character like yy then it's just 1


        # Initialize left pointer to 0
        # Initialize max_length to 0
        # Initialize an empty dictionary called known_chars

        # For each right pointer from 0 to the end of the string:
        #     current_char = character at index right
    
        # IF current_char is in known_chars AND its stored index is >= left:
        #     # We found a duplicate inside our current window!
        #     Move left to _______________
        
        # # Either way, record/update the character's newest position
        # Add or update current_char in known_chars with the index ________
    
        # # Calculate current window size and see if it's a new record
        # current_window_length = right - left + 1
        # max_length = maximum of (max_length vs current_window_length)

        # Return max_length

        left = 0
        max_length = 0
        known_chars = {}

        for right in range(len(s)):

            curr_char = s[right]

            if curr_char in known_chars and known_chars[curr_char] >= left:
                left = known_chars[curr_char] + 1
            
            known_chars[curr_char] = right 

            curr_window = right - left + 1
            max_length = max(max_length, curr_window)
        
        return max_length

            


        

