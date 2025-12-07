# https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s:str):
        """
        :type s: str
        :rtype: int
        """
        i,j=0,len(s)-1
        while(s[i]==' ' or s[j]==' '):
            if s[i]==' ':
                i+=1
            if s[j]==' ':
                j-=1
        s=s[i:j+1]
        s=s.split(' ')
        return len(s[-1])
    
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))