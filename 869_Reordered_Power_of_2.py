class Solution(object):
    def reorderedPowerOf2(self, n):
        count = {}
        for ch in str(n):
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        for i in range(31):  
            target = {}
            for ch in str(1 << i):
                if ch in target:
                    target[ch] += 1
                else:
                    target[ch] = 1
            
            if target == count:
                return True
        
        return False
        
