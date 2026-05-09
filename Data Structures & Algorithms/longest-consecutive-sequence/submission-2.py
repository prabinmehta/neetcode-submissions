from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
            


            
        