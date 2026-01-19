import random
import time
from typing import Tuple

# Konstanty
NUMBER_LENGTH = 4
SEPARATOR = "-" * 47


def generate_secret_number() -> str:

    digits = list(range(10))
    first_digit = random.choice(range(1, 10))  # První číslice nesmí být 0
    digits.remove(first_digit)
    
    secret = [str(first_digit)]
    for _ in range(NUMBER_LENGTH - 1):
        digit = random.choice(digits)
        secret.append(str(digit))
        digits.remove(digit)
    
    return ''.join(secret)


def validate_guess(guess: str) -> Tuple[bool, str]:
    
    # Kontrola, zda obsahuje jen číslice
    if not guess.isdigit():
        return False, "The guess must contain only digits!"
    
    # Kontrola délky
    if len(guess) != NUMBER_LENGTH:
        return False, f"The guess must be exactly {NUMBER_LENGTH} digits long!"
    
    # Kontrola, že nezačíná nulou
    if guess[0] == '0':
        return False, "The guess cannot start with zero!"
    
    # Kontrola duplicit
    if len(set(guess)) != len(guess):
        return False, "The guess cannot contain duplicate digits!"
    
    return True, ""


def calculate_bulls_and_cows(secret: str, guess: str) -> Tuple[int, int]:

    bulls = 0
    cows = 0
    
    # Počítání bulls
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
    
    # Počítání cows (pouze pro pozice, které nejsou bulls)
    for i in range(len(guess)):
        if secret[i] != guess[i] and guess[i] in secret:
            cows += 1
    
    return bulls, cows


def format_result(bulls: int, cows: int) -> str:
    
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    
    return f"{bulls} {bull_word}, {cows} {cow_word}"


def format_guesses(count: int) -> str:
    
    guess_word = "guess" if count == 1 else "guesses"
    return f"in {count} {guess_word}!"


def format_time(seconds: float) -> str:
   
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    else:
        minutes = int(seconds // 60)
        secs = seconds % 60
        minute_word = "minute" if minutes == 1 else "minutes"
        return f"{minutes} {minute_word} and {secs:.1f} seconds"


def print_intro() -> None:

    print("Hi there!") # Úvodní zpráva
    print(SEPARATOR)
    print(f"I've generated a random {NUMBER_LENGTH} digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)


def play_game() -> None:
    
    print_intro() # Hlavní herní smyčka
    
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()  # Zaznamenání času začátku hry
    
    while True:
        print("Enter a number:")
        print(SEPARATOR)
        guess = input(">>> ")
        
        # Validace vstupu
        is_valid, error_message = validate_guess(guess)
        if not is_valid:
            print(error_message)
            print(SEPARATOR)
            continue
        
        attempts += 1
        
        # Výpočet bulls a cows
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        
        # Kontrola výhry
        if bulls == NUMBER_LENGTH:
            elapsed_time = time.time() - start_time
            print("Correct, you've guessed the right number")
            print(format_guesses(attempts))
            print(f"It took you {format_time(elapsed_time)}")
            print(SEPARATOR)
            print("That's amazing!")
            break
        
        # Výpis výsledku
        print(format_result(bulls, cows))
        print(SEPARATOR)


if __name__ == "__main__":
    play_game()
