"""
This is basic password generator.
Author: @akerdogmus
"""

import sys
import random
import string

def main():
    """Main Func"""
    print("This is Password Generator.")
    length = int(input("\nEnter the length of password: "))
    pwd = pwd_generator(length)
    print("Password generated! -> ", pwd)
    try_decision = input("\nTry again? (y/n): ")
    if try_decision == "y":
        main()
    else:
        sys.exit()

def pwd_generator(length):
    """Password Generator Function"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all_strings = lower + upper + num + symbols

    temp = random.sample(all_strings, length)

    pwd = "".join(temp)

    return pwd

main()
