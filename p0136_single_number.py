
# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """        
        num=0
        for item in nums:
            num^=item
        return num
        
        
numList=[2,4,1,2,1]
print(Solution().singleNumber(numList))