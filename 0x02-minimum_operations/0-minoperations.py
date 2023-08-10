#!/usr/bin/python3
"""
module calculates the min operations
taken to copy and paste a character string
"""


def minOperations(n: int) -> int:
    """
    returns the min steps
    taken to get n chars
    """

    if n == 1:
        return 0

    # initialize the string array
    dp = [0] * (n + 1)

    for i in range(2, n+1):
        dp[i] = i
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i//j))

    return dp[n]
