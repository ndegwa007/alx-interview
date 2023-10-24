#!/usr/bin/python
"""prime game"""

def remove_multiples(nums, prime):
  """
  Removes the multiples of a number from a list of numbers.

  Args:
    nums: A list of numbers.
    prime: A prime number.

  Returns:
    A list of numbers with the multiples of the prime number removed.
  """

  new_nums = []
  for num in nums:
    if num % prime != 0:
      new_nums.append(num)

  return new_nums



def is_prime(num):
  """
  Checks if a number is prime.

  Args:
    num: A number.

  Returns:
    True if the number is prime, False otherwise.
  """

  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False

  return True



def find_prime(nums):
  """
  Finds the first prime number in a list of numbers.

  Args:
    nums: A list of numbers.

  Returns:
    The first prime number in the list, or None if there are no prime numbers in the list.
  """

  for num in nums:
    if is_prime(num):
      return num

  return None


def isWinner(x, nums):
  """
  Determines the winner of the game given the number of rounds and the set of numbers.

  Args:
    x: The number of rounds.
    nums: An array of n.

  Returns:
    The name of the player that won the most rounds, or None if the winner cannot be determined.
  """

  # Create a list to store the number of wins for each player.
  player_wins = [0, 0]

  # Create a set to store the prime numbers that Maria has chosen in each round.
  maria_chosen_primes = set()

  # Iterate over the number of rounds.
  for i in range(x):

    # Maria always goes first.
    maria_turn = True

    # While there are still prime numbers left, the players take turns choosing a prime number and removing it and its multiples from the set.
    while nums:

      # If it is Maria's turn, she chooses a prime number.
      if maria_turn:
        maria_prime = find_prime(nums)

        # If Maria has already chosen the prime number in the same round, she cannot choose it again.
        if maria_prime in maria_chosen_primes:
          continue

        # Otherwise, Maria adds the prime number to the set of chosen prime numbers.
        maria_chosen_primes.add(maria_prime)
      else:
        ben_prime = find_prime(nums)

      # Remove the prime number and its multiples from the set.
      nums = remove_multiples(nums, maria_prime if maria_turn else ben_prime)

      # Switch to the other player's turn.
      maria_turn = not maria_turn

    # If there are no numbers left in the set, the player whose turn it is wins the round.
    if not nums:
      player_wins[0 if maria_turn else 1] += 1

    # Otherwise, the round is a tie.
    else:
      player_wins[0] += 1
      player_wins[1] += 1

  # If Maria has more wins than Ben, she wins the game.
  if player_wins[0] > player_wins[1]:
    return "Maria"

  # If Ben has more wins than Maria, he wins the game.
  elif player_wins[1] > player_wins[0]:
    return "Ben"

  # If neither player has more wins than the other, the game is a tie.
  else:
    return None

