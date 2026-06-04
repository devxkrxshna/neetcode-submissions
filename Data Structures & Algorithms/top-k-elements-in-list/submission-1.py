class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict={}
        for i in range(len(nums)):
            my_dict[nums[i]]=my_dict.get(nums[i],0)+1
        arr=[]
        for num,count in my_dict.items():
            arr.append([count,num])
        arr.sort()

        res=[]
        while len(res)<k:
            val=arr.pop()[1]
            res.append(val)
   
        return res
            

        