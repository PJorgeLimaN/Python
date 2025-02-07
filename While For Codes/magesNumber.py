secret_number = 777
guess = 0

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while guess != secret_number:
    guess = int(input("\n\nGuess my number thee, or forever stuck you shall be!\n>"))

    if guess == secret_number: print("Well done, muggle! You are free now.")
    else: print("Ha ha! You're stuck in my loop!")
