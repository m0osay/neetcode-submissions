class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sort in python takes O(Nlgn(N))
        #we want O(N)
        #Two pointer is O(N)

        l,r = 0,1
        dictionary = {}

        for n in nums:
            if n in dictionary:
                return True
            else:
                dictionary[n] = n

            
        return False


        