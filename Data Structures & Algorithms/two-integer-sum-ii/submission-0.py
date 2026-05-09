class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            # print(i,j,numbers[i],numbers[j])
            a = numbers[i]+numbers[j]
            if a==target:
                return [i+1,j+1]
            elif a<target:
                i+=1
            elif a>target:
                j-=1
        return [-1,-1]
        