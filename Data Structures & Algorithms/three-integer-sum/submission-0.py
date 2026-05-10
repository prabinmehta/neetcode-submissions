class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i,j in enumerate(nums):
            s = set()
            # print("s is outisde",s)
            for k in nums[i+1:]:
                # print("j is and k is ",j,k)
                req = -(j+k)
                # print("req is ",req)
                if req in s:
                    # res.add(tuple(sorted(j,req,k)))
                    res.add(tuple(sorted((j, req, k)))) 
                    # print("res inside is if ",res)
                    s.add(k)
                    # print("s is inside if ",s)
                else:
                    s.add(k)
                    # print("s inside else is ", s)
        return [list(i) for i in res]
        