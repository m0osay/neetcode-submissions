class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Understand:
                - group all anagrams into a sublist. with same characters
            
            Approach:
                - sort each word: "".join(sorted(strs))
                - check if each word matches
                - make sort word hashup
                    - key: sort word, value, index: List[str]


        '''
        maps = {}
        for s in range(0,len(strs)):

            sorts_s = "".join(sorted(strs[s]))

            if sorts_s not in maps:
                maps[sorts_s] = [strs[s]]
            else: 
                lst = maps[sorts_s]
                lst.append(strs[s])
        
        final = []
        #loop through hashmap and make sublist
        keys = list(maps.keys())

        for d in keys: 
            final.append(maps[d])
        
        return final






        