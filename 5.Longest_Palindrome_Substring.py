class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        
        def findLongestPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        for i in range(len(s)):
            # odd-length palindrome
            odd_palindrome = findLongestPalindrome(i, i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome

            # even-length palindrome
            even_palindrome = findLongestPalindrome(i, i + 1)
            if len(even_palindrome) > len(res):
                res = even_palindrome
        
        return res
