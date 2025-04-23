class Solution(object):
    def countDays(self, days, meetings):
        meetings.sort()   
        free_days = 0
        prev_end = 0  
        
        for start, end in meetings:
            if start > prev_end + 1:
                free_days += (start - prev_end - 1)
            
            prev_end = max(prev_end, end)
        
        if prev_end < days:
            free_days += (days - prev_end)
        
        return free_days
        
