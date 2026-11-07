class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
  
        '''
        "UMPIRE"
        "Option 1: We could you a while loop and hashmap, and compare the frequence
        Option 2: We could you use a two pointer technique but this would be O(n^2)
        
       Edge #1: If the list s or t is null return false
       Edge #2: If list s and t are null return true?
       
       Case #1:
            s = "mop" & t = "pom" -> true
       Case #2: 
            s = "plane" & t = "lane" -> false bc p is missing for t      
        Case #3:
        s = "a" & t ="tt" -> false b/c s and t arent the same size
        ''' 

        if s is None or t is None:

            return False
        elif len(s) != len(t):

            return False
        

        frequencyS = {}
        for i in s:
       # if i < len(s):
            if i in frequencyS:
                num = frequencyS[i]
                frequencyS[i] = num + 1
            else:
                frequencyS[i] = 1
                
       
    #frequencyT = {}
    
        for char in t:
            if char in frequencyS  and frequencyS[char] > 0 :
                num = frequencyS[char]
                frequencyS[char] = num - 1
            else:
                return False
    
        return True
    '''
    i = 0
    while (i < len(S)){
        #check for S
        if i < len(s):
            if s[i] in frequencyS:
                num = frequencyS[s[i]]
                frequencyS[s[i]] = num + 1
            else:
                frequencyS[s[i]] = 1
                
        #check for t
        if i < len(t):
            if t[i] in frequencyT:
                num = frequencyT[t[i]]
                frequencyT[t[i]] = num + 1
            else:
                frequencyT[t[i]] = 1
        

    }
'''
    #loop trhough

        