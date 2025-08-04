class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)

        for p in range(1, n - 2): 
            inc1 = True
            for i in range(p): 
                if nums[i] >= nums[i+1]:
                    inc1 = False
                    break
            if not inc1:
                continue

            for q in range(p + 1, n - 1): 
                inc2 = True
                for i in range(p, q): 
                    if nums[i] <= nums[i+1]:
                        inc2 = False
                        break
                if not inc2:
                    continue

                inc3 = True
                for i in range(q, n - 1): 
                    if nums[i] >= nums[i+1]:
                        inc3 = False
                        break
                
                if inc3:
                    return True
        
        return False
