class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            d[i]=d.get(i,0)-1
        for i in d:
            if d[i]!=0:
                return False
        return True
        