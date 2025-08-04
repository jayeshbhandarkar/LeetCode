class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        res = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                landStart = landStartTime[i]
                landEnd = landStart + landDuration[i]
                waterStart = max(waterStartTime[j], landEnd)
                waterEnd = waterStart + waterDuration[j]
                res = min(res, waterEnd)
    
                waterStart = waterStartTime[j]
                waterEnd = waterStart + waterDuration[j]
                landStart = max(landStartTime[i], waterEnd)
                landEnd = landStart + landDuration[i]
                res = min(res, landEnd)
    
        return res
        
