class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        left_answer=[1]*len(nums)
        for i in range(len(nums)):
            left_answer[i]=prefix   
            prefix*= nums[i]
        # right_answer=[1]*len(nums)
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            left_answer[i]*=suffix
            suffix*=nums[i]

        return left_answer