from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for key,val in count.items():
            buckets[val].append(key)
        return [num for bucket in reversed(buckets) for num in bucket][:k]
        # return [num for bucket in reversed(buckets) for num in bucket][:k]

        

        