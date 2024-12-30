#!/usr/bin/python3

"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds
        nums (list): List of integers, where each integer n
        represents the range 1 to n for a round

    Returns:
        str: Name of the player with the most wins
        ("Maria" or "Ben"), or None if there is a tie
    """
    if x < 1 or not nums:
        return None

    def sieve_of_eratosthenes(n):
        """Generates a list of prime numbers up to n."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, n + 1, i):
                    primes[multiple] = False
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the total number of primes up to n
        primes_up_to_n = prime_count[n]

        # Maria wins if the number of primes is odd, Ben wins if it's even
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))