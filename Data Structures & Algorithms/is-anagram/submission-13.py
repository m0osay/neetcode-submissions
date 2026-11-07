class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #expected time complexity: O(N + M)
        #expected space complexity: ?
        '''
            Understand:
                anagrams two strings have the same characters no matter what order
            
            match:
                - bad
                    - Brute force: two loops? bad
                - efficent
                    - hashmap

                    - sort then compare?
                        time-complexty: O((M + N)Log(M + N))

            
            plan:
                - loop through s
                    - add s to dicitionary with k = string s, value = count


        '''

        if len(s) != len(t):
            return False

        hashmap = {}
        total_s = len(s)

        for char in s:
            if char in hashmap:
                hashmap[char] = hashmap[char] + 1
            else:
                hashmap[char] = 1


        print(hashmap)
        
        for char in t:
            if char in hashmap and hashmap[char] < 1: 
                return False
            if char in hashmap:
                count = hashmap[char]
                hashmap[char] = count - 1
                total_s -= 1
        
        print(hashmap)
        if total_s == 0:
            return True
        else:
            return False
            


        





        