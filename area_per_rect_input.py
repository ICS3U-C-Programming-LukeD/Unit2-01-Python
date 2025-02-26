#!/usr/bin/env python3

# Created By: Luke
# Date: Feb 20, 2025
# Takes the input of a user and performs math calculations

import math  # Imports the math module


def main():
    #
    length = int(
        input("Enter length of the rectangle (mm): ")
    )  # Gets the users input for the length and converts it into an integer
    width = int(
        input("Enter width of the rectangle (mm): ")
    )  # Gets the users input for the width and converts it into an integer
    print()
    print(
        "The area is {}".format(length * width) + "mm"
    )  # Performs the area calculation and prints it
    print(
        "The perimeter is {}".format(2 * (length + width)) + "mm"
    )  # Performs the perimeter calculation and prints it


if __name__ == "__main__":
    main()
