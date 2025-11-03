class Solution(object):
    def minCost(self, colors, neededTime):
        totalTime = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                totalTime += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return totalTime
        
