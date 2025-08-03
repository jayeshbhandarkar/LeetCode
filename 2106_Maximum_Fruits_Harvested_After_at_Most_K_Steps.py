class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        max_fruits = 0
        total = 0
        i = 0

        for j in range(n):
            total += fruits[j][1]

            while i <= j:
                left_pos, right_pos = fruits[i][0], fruits[j][0]
                steps = min(
                    abs(startPos - left_pos) + (right_pos - left_pos),
                    abs(startPos - right_pos) + (right_pos - left_pos)
                )
                if steps <= k:
                    break
                total -= fruits[i][1]
                i += 1

            max_fruits = max(max_fruits, total)

        return max_fruits
