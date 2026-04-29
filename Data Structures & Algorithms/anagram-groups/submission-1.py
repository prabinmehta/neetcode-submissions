from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            c = [0]*26
            for j in i:
                c[ord(j)-ord('a')]+=1
            key = tuple(c)
            group[key].append(i)
        return list(group.values())
        