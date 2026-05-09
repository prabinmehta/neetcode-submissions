from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a hashmap of numbers and the length until there
        # check if the number exists, if exists ignore
        # else check for 
        # n-1 -> take max(n-1+1,n-1)
            # check for n+1: if exists: n+1 -> max(n+1,n+1)
        # else n =1
        #nums=[2,20,4,10,3,4,5]
        num_set = set(nums)
        res =0 
        for i in nums:
            if i-1 not in num_set:
                length = 1
                j = i
                while j+1 in num_set:
                    length+=1
                    j=j+1
                res= max(res,length)
        return res
            


            
        