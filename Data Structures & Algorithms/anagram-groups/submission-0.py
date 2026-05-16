class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        my_dict = {}


        for word in strs:
            temp_sort = ''.join(sorted(word))

            if temp_sort not in my_dict:
                my_dict[temp_sort] = [word]
            else:
                my_dict[temp_sort].append(word)

        return list(my_dict.values())

        