class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Two pointer technique?
        Recursion?


        Case #1:
        nums = {4,5,9}, target = 9->{0,1}
        Case #2:
        nums = {1,5,9,4}, target = 5->{0,4}
        Case #3:
        nums = {}, target = 9->{0,1}

        Edge #1:
        nums = {4,5,3}, target = 10->{} <- wont happen
        Edge #2:
        nums = {}, target = 10->{}
        Edge #3:
        nums = {3,2,1}, target = 0->{}
        '''
        if (nums is None):
            return []

        left, right = 0,len(nums) - 1

        while( left < len(nums)):
            print("Left" + str(left))
            print("right" + str(right))
            #we match our values
            if right != left and nums[left] + nums[right] == target:
                lst =  [left, right]
                print(left)
                return lst
            
            right -= 1

            if left == right:
                right = len(nums) - 1
                left += 1

    