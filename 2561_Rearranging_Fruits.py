class Solution(object):
    def minCost(self, basket1, basket2):
        n = len(basket1)
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        mini = min(basket1 + basket2)

        res1 = []
        for i in count1:
            c1 = count1[i]
            c2 = count2.get(i, 0)
            if (c1 + c2) % 2 != 0:
                return -1
            if c1 > c2:
                res1.extend([i] * ((c1 - c2) // 2))

        res2 = []
        for i in count2:
            c2 = count2[i]
            c1 = count1.get(i, 0)
            if (c1 + c2) % 2 != 0:
                return -1
            if c2 > c1:
                res2.extend([i] * ((c2 - c1) // 2))

        res1.sort()
        res2.sort(reverse = True)

        answer = 0
        for i in range(len(res1)):
            x = res1[i]
            y = res2[i]
            answer += min(2 * mini, min(x, y))

        return answer
