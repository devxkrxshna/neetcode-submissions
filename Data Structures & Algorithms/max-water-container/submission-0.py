class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        width = len(heights)-1
        l=0
        r=len(heights)-1
        while l<r:
            min_height= min(heights[l], heights[r])
            cur_area= min_height*width
            max_area= max(cur_area,max_area)
            if heights[l]<=heights[r]:
                l+=1
                width-=1
            else:
                r-=1
                width-=1
        return max_area

            
        