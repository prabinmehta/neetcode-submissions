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
        d= defaultdict(int)
        for i in nums:
            if i in d:
                continue
            elif i not in d:
                d[i]=1 #{2:1,20:1,4:3,10:1,3:2}
                if i-1 in d:
                    d[i]= d[i]+d[i-1]
                if i+1 in d:
                    d[i+1] = max(d[i+1],d[i]+1)
                    j = i+1
                    while j+1 in d:
                        d[j+1]= max(d[j+1],d[j]+1)
                        j=j+1
        res = 0 
        for i in d:
            res = max(res, d[i])
        return res

            
        