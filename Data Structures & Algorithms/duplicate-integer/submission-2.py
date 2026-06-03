class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict={}
        for n in nums:
            my_dict[n]= my_dict.get(n,0)+1
            
        for k,v in my_dict.items():
            if v>1:
                return True
        return False