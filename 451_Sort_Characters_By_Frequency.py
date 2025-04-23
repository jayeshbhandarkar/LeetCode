class Solution(object):
    def frequencySort(self, s):
        count = {}
        
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = ""
        for ch, freq in sorted_chars:
            result += ch * freq  

        return result
