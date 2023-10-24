#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """get winner"""
    if x <= 0:
        return None

    def is_prime(num):
        """check for primes"""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_winner(n):
        """find the winner based on is_prime"""
        if n <= 1:
            return "Ben"
        if n % 2 == 0:
            return "Ben"
        if is_prime(n):
            return 'Maria'
        return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = calculate_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
