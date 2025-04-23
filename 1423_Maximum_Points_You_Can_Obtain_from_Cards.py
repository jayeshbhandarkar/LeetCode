class Solution(object):
    def maxScore(self, cardPoints, k):
    
        left_sum = sum(cardPoints[:k])
        max_score = left_sum
        right_sum = 0

        for i in range(1, k+1):
            right_sum += cardPoints[-i]
            left_sum -= cardPoints[k-i]
            max_score = max(max_score, left_sum + right_sum)

        return max_score
        
