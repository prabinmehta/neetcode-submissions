from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for i in strs:
            l = Counter(i)
            found=False
            for j in s:
                if Counter(j)==l:
                    found=True
                    s[j]=s[j]+[i]
            if found==False:
                s[i]=[i]
        res=[]
        for i in s:
            res.append(s[i])
        return res

            
        