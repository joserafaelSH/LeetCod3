class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total, local = 0,0

        for i in range(len(prices)-1):
            aux = local + prices[i+1] - prices[i]

            local = 0 if 0>aux else aux
            total = total if total>local else local

        return total