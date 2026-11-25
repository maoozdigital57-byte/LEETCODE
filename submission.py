class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')   # shuru mein bohat bada number
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price              # sasta price mila, update karo
            else:
                profit = price - min_price     # aaj bechun to profit?
                if profit > max_profit:
                    max_profit = profit        # bada profit mila, update karo

        return max_profit