
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        if rowIndex==0:
            return [1]
        pRow=[0]*(rowIndex+1)
        pRow[0]=1

        for i in range(rowIndex+1):
            for j in range(i, 0, -1):
                pRow[j]+=pRow[j-1]

        return pRow
size=2
print(Solution().getRow(size))
        