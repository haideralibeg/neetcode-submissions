class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        longest_sequence = 0

        num_set = set(nums) # converts to a set and removes all dupes


        for n in num_set:

            if n - 1 not in num_set:
                current_num = n
                current_sequence = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1
                
                longest_sequence = max(longest_sequence, current_sequence)

                
        return longest_sequence



