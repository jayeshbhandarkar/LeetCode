class Solution(object):
    def numberToWords(self, num):
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return "Zero"

        result = []

        if num >= 1000000000:
            result.append(self.numberToWords(num // 1000000000) + " Billion")
            num %= 1000000000

        if num >= 1000000:
            result.append(self.numberToWords(num // 1000000) + " Million")
            num %= 1000000

        if num >= 1000:
            result.append(self.numberToWords(num // 1000) + " Thousand")
            num %= 1000

        if num >= 100:
            result.append(ones[num // 100] + " Hundred")
            num %= 100

        if num >= 20:
            result.append(tens[num // 10])
            num %= 10
    
        if num >= 10:
            result.append(teens[num - 10])
            num = 0

        if num > 0:
            result.append(ones[num])

        return " ".join(result)
