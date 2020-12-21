#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        '''
        1.找到R的位置
        2.向4个方向遍历，找到第一个P，该方向停止遍历
        3.找到第一个B，该方向停止遍历
        '''
        #定义上下左右
        dx,dy = [-1,1,0,0],[0,0,-1,1]
        x,y,res = 0,0,0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    #记录位置
                    x,y = i,j
        for i in range(4):
            step = 0
            while True:
                xx = x + step*dx[i]
                yy = y + step*dy[i]
                if xx<0 or xx>=8 or yy<0 or yy>=8 or board[xx][yy] == 'B':
                    break
                if board[xx][yy] == 'p':
                    res += 1
                    break
                step += 1
        return res
# @lc code=end

