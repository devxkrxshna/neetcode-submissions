import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for num in nums:
            counter[num]= counter.get(num,0)+1
        
        heap=[]
        for val, count in counter.items():
            heapq.heappush(heap,[count,val])
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for val in heap:
            res.append(val[1])
        return res

        