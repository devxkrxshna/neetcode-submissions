class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for num in nums:
            counter[num]= counter.get(num,0)+1
        
        heap=[]
        for val,count in counter.items():
            heapq.heappush(heap,[-count,val])
            print(heap)
        res=[]
        for i in range(0,k):
           val= heapq.heappop(heap)[1]
           print(val)
           res.append(val)
        return res
