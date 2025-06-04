class Solution(object):
    def numRescueBoats(self, people, limit):
        left = 0
        right = len(people) - 1
        boats = 0
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats
        
