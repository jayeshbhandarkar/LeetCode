class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        n = mountainArr.length()
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        def binary_search(l, r, target, ascending=True):
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid

                if ascending:
                    if val < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if val < target:
                        r = mid - 1
                    else:
                        l = mid + 1
                        
            return -1

        index = binary_search(0, peak, target, True)
        if index != -1:
            return index

        return binary_search(peak + 1, n - 1, target, False)
