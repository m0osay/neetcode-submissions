class Solution:

    def compare_words(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
       
        chars_to_match = list(word2)
        
        for char in word1:
            if char in chars_to_match:
                
                chars_to_match.remove(char)
            else:
               
                return False
                
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Understand:
                -> Order words that are same in different order in a sublist
                -> Time complexity O(1)
                -> ALL lower case
                -> Two pointer appraoch:
                    -> i and j is at the end, check each string and 
                    -> Use Hashmap to store similar words

        '''

        i = 0
        j = len(strs) - 1
        freq = {}
        # Make a copy because we modify strs in-place
        original_strs = list(strs)

        while i < len(strs): 
            if j >= 0: 
                if strs[i] != "DONE" and strs[j] != "DONE":
                   
                    result = self.compare_words(strs[i], strs[j])
                    if result:
                        root_word = original_strs[i]
                        if root_word in freq:
                            freq[root_word].append(strs[j])
                        else:
                            freq[root_word] = [strs[j]]
                        
                        if i != j:
                            strs[j] = "DONE"
                        else:
                            strs[i] = "DONE"
                
                j -= 1
            else:
                j = len(strs) - 1
                i = i + 1
        
        final_result = []
        for key in freq:
            final_result.append(freq[key])
        return final_result