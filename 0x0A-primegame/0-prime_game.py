#!/usr/bin/python3

def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
pridef isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
printdef isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Bedef isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prdef isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game and returns the winner """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        removed = [False] * (n + 1)
        
        for prime in primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
print("Winner: {}".format(isWinner(x, nums)))  # Output: Winner: Benn primes:
            if not removed[prime]:
                # When a player picks a prime, they remove it and its multiples
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
                turn = 1 - turn  # Switch turns

        # If turn is 0 after the loop, it means Ben has no moves left
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins >
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
print("Winner: {}".format(isWinner(x, nums)))  # Output: Winner: Ben
print("Winner: {}".format(isWinner(x, nums)))  # Output: Winner: Ben
