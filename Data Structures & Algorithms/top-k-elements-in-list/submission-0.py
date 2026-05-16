class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # we need to sort the array the answer will be towards the end of the array
        # do loop through the array and store duplicate values in a dictionary/map?
        # and then we also have to count the number of duplicates to see what number is the most frequent
        # need to make sure to return the amount of values that k requires. How do we do that?
        # I think temp store dupes in a map and then once we have our values we return the value not the index. 
        

        count = {}

        for n in nums:

            # put the list in the dictionary
            count[n] = 1 + count.get(n, 0) # this is to increment. Can't do count[n] = count[n] + 1, .get() -> If you don't find n, just pretend it's 0

        # the result is the sorted dictionary keys in reverse and it only gives you the k amount

        res = sorted(count.keys(),key=lambda x: count[x], reverse=True)

        # return the k values 
        return res[:k]