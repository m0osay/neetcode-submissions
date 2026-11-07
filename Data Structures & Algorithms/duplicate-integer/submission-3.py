class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Understand: 
        - So bascially we want want to return true if we have duplicate vlaue

        Plan:
        Case 1:
          nums = {3,4,3} -> true
        Case 2:
            nums = {6,5} -> false

        The only edged case if the list it empty/null or if it is size one
        Edge case 1:
            nums = {} -> false
        
        Edge case 2:
            nums = {4} -> false
        '''
        
        if nums is None:
            return False
        elif len(nums) == 1:
            return False


        dictionary = { }

        for i in nums:
            if i in dictionary:
                return True
            else:
                dictionary[i] = 1
        #print(list(dictionary))
        print("Hello")
        return False


         