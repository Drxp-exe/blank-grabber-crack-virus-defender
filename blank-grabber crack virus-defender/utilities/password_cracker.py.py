import itertools

def bruteforce_password(target, charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            guess = ''.join(attempt)
            print(f"Trying: {guess}")
            if guess == target:
                print(f"Password found: {guess}")
                return
    print("Password not found.")

bruteforce_password("abc", "abcdefghijklmnopqrstuvwxyz", 4)
