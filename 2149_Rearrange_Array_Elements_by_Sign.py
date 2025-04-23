class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        ans = []
        
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        
        return ans
   
