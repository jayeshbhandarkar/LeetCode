class Solution(object):
    def totalFruit(self, fruits):
        fruit1 = None
        fruit2 = None
        last_fruit1 = 0
        curr_count = 0
        max_count = 0

        for fruit in fruits:
            if fruit == fruit1 or fruit == fruit2:
                curr_count += 1
            else:
                curr_count = last_fruit1 + 1
        
            if fruit == fruit1:
                last_fruit1 += 1
            else:
                last_fruit1 = 1
                fruit2 = fruit1
                fruit1 = fruit

            max_count = max(max_count, curr_count)

        return max_count
