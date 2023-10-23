#!/usr/bin/python3
"""bottom-up approach"""
import sys


def makeChange(coins, total):
    """list  of all possible coins"""
    if total < 0:
        return 0
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0
   

    for amount in range(1, total+1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == sys.maxsize:
        return -1
    return dp[total]
