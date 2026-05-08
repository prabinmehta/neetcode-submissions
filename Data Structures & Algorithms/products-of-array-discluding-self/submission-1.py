class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        havezero = 0
        output =[]
        for i in nums:
            if i==0:
                havezero+=1
            else:
                prod*=i
        for i in nums:
            if i==0 and havezero==1:
                output.append(prod)
            else:
                if havezero>=1:
                    output.append(0)
                else:
                    output.append(prod//i)
        return output

        