#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [price for price in prices]
        if len(prices) == 1:
            print(ans)
        for i in range(len(prices)-1):
            j = i+1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break
                j += 1
        return ans
# @lc code=end

