class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        '''
        So no matter how big the array is we need to organize it in triples that == 0
        and from that array if possible rearrange the i, j, k to see which indicies add to 0
        we also don't have to use all the elements in the array 
        only the triples if they add to 0 (if they add)

        So in a loop set the first element as a temp value then look for the inverse of 
        that by adding 2 other elements from the array and if there is a match then add 
        the temp to the triple

        '''
        output = []

        # first sort the array
        nums.sort()

        # outer loop for temp value (anchor)
        for i in range(len(nums)):


            # make sure it does not run the dupe number
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            temp = nums[i]

            # look for 2 numbers to the right of temp that add up to the inverse of temp

            left = i + 1
            right = len(nums) - 1

            while left < right:

                current_sum = nums[left] + nums[right]

                if current_sum < -temp:
                    left += 1
                elif current_sum > -temp:
                    right -= 1
                
                else:
                    # combine temp, left, right and then append to the output
                    triple = [temp, nums[left], nums[right]]
                    output.append(triple)

                    # keep going
                    left += 1
                    right -= 1

                    # skipping dupes so you don't have the same values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return output













