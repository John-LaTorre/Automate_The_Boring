"""Silly name generator from Chapter 1 of Impractical Python Projects by No Starch Press"""

import sys
import random

def main():
    print("Welcome to the Silly Name Generator.\n")
    print("Just a bunch of silly names that are not related to anything.\n")

    first = ('Baby Oil', 'Buttocks', 'Chad', 'Cleet', 'Cornbread', 'Dark Skies',
    'Elphonso', 'Fancypants', 'Greasy Jim', 'Jimbo', 'Scratchensniff', 'Snoobs',
    'Sweet Tea', 'Wheezy Joe')

    last = ('Appleyard', 'Bloominshine', 'Clutterbuck', 'Cocktoasten', 'Goodpasture',
    'Hooperbag', 'Jefferson', 'Jenkins', 'Pinkerton', 'Quakenbush', 'Snuggleshine',
    'Wallbanger', 'Wigglesworth')

    while True:
        first_name = random.choice(first)

        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
