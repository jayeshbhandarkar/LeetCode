class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = (left + right ) // 2
            ans = guess(mid)

            if ans == 0:
                return mid

            elif ans == -1:
                right = mid - 1

            else:
                left = mid + 1
