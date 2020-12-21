#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index.append((i,j))
        
        for i,j in index:
            matrix[i] = [0] * len(matrix[i])
            for k in range(len(matrix)):
                matrix[k][j] = 0
        return matrix 
# @lc code=end

