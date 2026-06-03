class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            # print(i)
            if (target-nums[i]) in my_dict:
                # print(nums[i])
                return [my_dict[target-nums[i]],i]
            else:
                my_dict[nums[i]]=i
                # print(my_dict)
        return[0,0]
            

        