class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #convert string to list
        
        s1 = sorted(s)
        t2 = sorted(t)

        s = "".join(s1)
        t = "".join(t2)

        if s != t:
            return False
    
        return True

        


        