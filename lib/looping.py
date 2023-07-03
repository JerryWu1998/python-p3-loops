#!/usr/bin/env python3


def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    int_list = [ints * ints for ints in int_list]
    return int_list


def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz\n")
        elif i % 3 == 0:
            print("Fizz\n")
        elif i % 5 == 0:
            print("Buzz\n")
        else:
            print(f"{i}\n")
