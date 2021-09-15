#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program calculates the circumference of a circle
#   with user input

import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("circumference is {} mm^2.".format(circumference))
    print("Done.")


if __name__ == "__main__":
    main()
