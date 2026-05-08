class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # havezero = 0
        # output =[]
        # for i in nums:
        #     if i==0:
        #         havezero+=1
        #     else:
        #         prod*=i
        # for i in nums:
        #     if i==0 and havezero==1:
        #         output.append(prod)
        #     else:
        #         if havezero>=1:
        #             output.append(0)
        #         else:
        #             output.append(prod//i)
        # return output
        prodleft = [1]*len(nums)
        prodright = [1]*len(nums)
        prod = 1
        for i,j in enumerate(nums):
            if i==0:
                prodleft[i]=j
            else:
                prodleft[i]=prodleft[i-1]*j
        for i in range(len(nums)-1,0,-1):
            if i==len(nums)-1:
                prodright[i]=nums[i]
            else:
                prodright[i]=prodright[i+1]*nums[i]
        res =[]
        for i in range(len(nums)):
            if i==0:
                res.append(prodright[i+1])
            elif i==len(nums)-1:
                res.append(prodleft[i-1])
            else:
                res.append(prodleft[i-1]*prodright[i+1])
        return res        