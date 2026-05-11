class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        i=0
        j=0
        maxi=0
        while j<len(s):
            if s[j] in ss:
                maxi= max(maxi,len(ss))
                while s[j] in ss:
                    ss.remove(s[i])
                    i+=1
            else:
                ss.add(s[j])
                j+=1
        maxi= max(maxi,len(ss))
        return maxi


        