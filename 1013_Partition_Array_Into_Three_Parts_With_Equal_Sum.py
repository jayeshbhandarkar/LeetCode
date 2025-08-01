class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)

        if total % 3 != 0:
            return False

        n = len(arr)
        ans = total // 3
        cur_sum = 0
        count = 0

        for i in range(n):
            cur_sum += arr[i]

            if cur_sum == ans:
                count += 1
                cur_sum = 0

                if count == 2 and i < n - 1:
                    return True

        return False
        
