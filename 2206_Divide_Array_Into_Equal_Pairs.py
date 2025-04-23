class Solution(object):
    def divideArray(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num_count in count.values():
            if num_count % 2 != 0:
                return False  
        
        return True
