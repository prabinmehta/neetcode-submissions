class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,j in enumerate(nums):
            # print(i,j)
            k = target - j
            if k in s:
                return [s[k],i]
            else:
                s[j]=i
        return [-1,-1]
        