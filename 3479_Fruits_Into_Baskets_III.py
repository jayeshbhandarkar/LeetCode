class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        s = 1

        while s < n:
            s *= 2

        tree = [0] * (2 * s)
        for i in range(n):
            tree[s + i] = baskets[i]

        for i in range(s - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        unplaced = 0  

        for f in fruits:
            if tree[1] < f:
                unplaced += 1
                continue

            i = 1
            while i < s:  
                if tree[2 * i] >= f:
                    i = 2 * i
                else:
                    i = 2 * i + 1

            pos = i - s 
            tree[i] = -1
            i //= 2

            while i > 0:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i //= 2

        return unplaced
