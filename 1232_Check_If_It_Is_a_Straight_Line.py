class Solution(object):
    def checkStraightLine(self, coordinates):
        n = len(coordinates)
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for i in range(2, n):
            x3, y3 = coordinates[i]
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                return False

        return True
