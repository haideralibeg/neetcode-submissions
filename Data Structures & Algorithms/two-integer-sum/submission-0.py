class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        first we create a dictionary that maps each number in the array to its index - 
		[2,4,7,9] - [0,1,2,3]
		
		then we have another loop that goes through the array again and we find the difference 
		betweeen the target and the current number in the array
		
		then we check to see if the difference is actually there in the dictionary and if it's
		not on the same index 
		
		if the difference is there then we returnt the index of the target numebr and the index 
		of the difference. 

        '''



        # i is the current index and n is the number

        indicies = {}

        for i, n in enumerate(nums):
            indicies[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n

            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]
        
        return []

