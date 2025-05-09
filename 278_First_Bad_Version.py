# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low, high = 0, n

        while low <= high:
            mid = low + (high - low) // 2

            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
        
