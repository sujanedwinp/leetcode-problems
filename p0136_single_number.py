
# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        
        newlist=[]
        for item in nums:
            print(f"{item} : first {nums.index(item)} || last{nums[::-1].index(item)}") 
            firstIndex=nums.index(item)
            lastIndex=nums[::-1].index(item)
            if firstIndex+lastIndex==len(nums)-1:
                return item
        
    

        
numList=[2,1]
print(Solution().singleNumber(numList))