import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            v1 = -heapq.heappop(heap)
            v2 = -heapq.heappop(heap)
            l = v1-v2 if v1>v2 else v2-v1 if v2>v1 else 0
            heapq.heappush(heap,-l)
        return -heap[0]
            


        