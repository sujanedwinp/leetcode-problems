
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        if rowIndex==0:
            return [1]
        
        pascal=[[1]]
        
        for level in range(1, rowIndex+1):
            pascalRow=[1]
            for pCol in range(1, level):
                sum=pascal[level-1][pCol-1]+pascal[level-1][pCol]
                pascalRow.append(sum)
            pascalRow.append(1)
            pascal.append(pascalRow)
            

        return pascal[rowIndex]
size=0
print(Solution().getRow(size))
        