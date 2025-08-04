class Solution(object):
    def maxBalancedShipments(self, weight):
        n = len(weight)
        cnt = 0
        max_wgt = weight[0]
        start = 0

        for i in range(1, n):
            max_wgt = max(max_wgt, weight[i])
            if weight[i] < max_wgt:
                cnt += 1
                if i + 1 < n:
                    max_wgt = weight[i + 1]
                start = i + 1
                i = start 

        return cnt
