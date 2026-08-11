from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = [ [] for i in range(len(nums))]
        for i in freq:
            res[freq[i]-1].append(i)
        result = []
        for i in range(len(res)-1,-1,-1):
            result.extend(res[i])
            if len(result)>=k:
                return result[:k]

            

