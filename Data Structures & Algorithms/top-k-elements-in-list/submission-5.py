class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for num in nums:
            counter[num]= counter.get(num,0)+1
        counter_arr=[[] for i in range(len(nums)+1)]
        for val,count in counter.items():
            counter_arr[count].append(val)
        res=[]

        for i in range(len(nums),0,-1):
            for num in counter_arr[i]:
                res.append(num)
            if len(res)==k:
                return res
            
    
            
            
            