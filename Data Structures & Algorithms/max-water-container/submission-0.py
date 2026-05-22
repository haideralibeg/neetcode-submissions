class Solution:
    def maxArea(self, heights: List[int]) -> int:


        # Go through the array, don't sort  
        # Have a pointer on the left and right 
        # left at the start, right at the end 
        # record max area 
        # if the height of left is bigger then shift right 1 towards the center 
        # if the height of right is bigger then shift left 1 towards the center
        # if they are both equal then move one of the pointers 


        left = 0 
        right = len(heights) - 1
        area = 0

        while left < right:

            wid = right - left 
            current_height = min(heights[left], heights[right]) # the max height container can have 

            current_area = wid * current_height
            area = max(area, current_area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return area

                

            