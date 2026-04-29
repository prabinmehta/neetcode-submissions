from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i]+=1
        freqval = defaultdict(list)
        # print(freq)
        for i in freq:
            freqval[freq[i]].append(i)
        # print(freqval)
        s = sorted(freqval.keys(), reverse=True) 
        res = []
        for i in s:
            res.extend(freqval[i])
            if len(res)>=k:
                return res[:k]
        # result = []
        # for key in s:
        #     result.extend(freqval[key])   # add all nums with that frequency
        #     if len(result) >= k:
        #         return result[:k] 

        