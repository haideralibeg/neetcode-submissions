class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

       
        zero_counter = nums.count(0) 
        total_prod = 1

        for num in range(len(nums)):
            if nums[num] == 0: 
                continue # skip the 0 
            total_prod *= nums[num]
        
        output = []

        for num in nums:

            if zero_counter == 0:
                output.append(total_prod // num) # no zeros then divide by total product

            elif zero_counter == 1:

                if num == 0:
                    output.append(total_prod) # one zero then return total product
                else:
                    output.append(0) 
            else:
                output.append(0)


        return output

        


            