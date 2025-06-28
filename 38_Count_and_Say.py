class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"

        result = "1"

        for _ in range(2, n + 1):
            temp = ""
            count = 1

            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    temp += str(count) + result[j - 1]
                    count = 1

            temp += str(count) + result[-1]
            result = temp

        return result
