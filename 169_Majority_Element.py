class Solution(object):
    def majorityElement(self, nums):
        count = 0
        elements = None

        for num in nums:
            if count == 0:
                elements = num
            if num == elements:
                count+=1
            else:
                count-=1
    
        return elements
    
