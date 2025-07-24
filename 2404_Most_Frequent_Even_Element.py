class Solution(object):
    def mostFrequentEven(self, nums):
        freq = {}

        for num in nums:
            if num % 2 == 0:
                if num in freq:
                    freq[num] += 1

                else:
                    freq[num] = 1

        if not freq:
            return -1

        maxi = -1
        res = -1

        for num in freq:
            if freq[num] > maxi:
                maxi = freq[num]
                res = num

            elif freq[num] == maxi:
                if res > num:
                    res = num

        return res
        
