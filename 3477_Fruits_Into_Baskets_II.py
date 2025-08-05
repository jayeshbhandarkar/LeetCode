class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        used = [False] * n  
        unplaced = 0

        for i in range(n):
            placed = False

            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break

            if not placed:
                unplaced += 1

        return unplaced
 
