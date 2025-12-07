
# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        
        pascal=[[1]]
        
        for level in range(1, numRows):
            pascalRow=[1]
            for pCol in range(1, level):
                sum=pascal[level-1][pCol-1]+pascal[level-1][pCol]
                pascalRow.append(sum)
            pascalRow.append(1)
            pascal.append(pascalRow)
            

        return pascal
size=5
print(Solution().generate(size))