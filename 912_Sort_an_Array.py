class Solution:
    def sortArray(self, nums):
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            res = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
                    
            res.extend(left[i:])
            res.extend(right[j:])
            
            return res

        return mergeSort(nums)
