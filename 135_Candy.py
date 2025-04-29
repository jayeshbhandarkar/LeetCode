class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        arr = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                arr[i] = arr[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i+1] + 1, arr[i])

        return sum(arr)
                
