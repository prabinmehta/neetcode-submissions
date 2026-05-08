from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [ [] for i in range(len(nums)+1)]
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        print(d)
        for j in d:
            res[d[j]].append(j)
        result = []
        for bucket in res[::-1]:
            result.extend(bucket)
            if len(result)>=k:
                return result[:k]

        