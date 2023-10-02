#!/usr/bin/env python3

# Created by: souleye keita
# Created on: oct. 2, 2023
# This program calculates and displays the area and perimeter of a
# circle with radius 22 mm.
import math


def main():
    print("For a circle that has a radius")
    print("of 22 mm:")
    print("")
    print("Area = {} mm^2".format(round(math.pi * 22**2, 2)))
    print("Perimeter = {} mm".format(round(2 * math.pi * 22, 2)))


if __name__ == "__main__":
    main()
