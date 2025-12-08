
# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==" ":
            return True
        news=""
        for ch in s:
            if ch.isalnum():
                news+=ch.lower()
        print(news)
        return news==news[::-1]
        
s=".../-.."
print(Solution().isPalindrome(s))