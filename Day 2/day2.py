import os
os.chdir(r'C:\Users\Thatcher\Desktop\Coding Stuff\Advent of Code\Day 2')        ##Was getting error without changing directory

with open('input.txt') as file:
    text = file.read().replace(" ", "").split("\n")   ##Create list of all items and get rid of spaces

text.pop()           ##Get rid of " " item and end of list
text2 = text.copy()     ##Copy so we can use list twice

interpret = {    ##Dictionary of all possible cases and their score equivalent
    "AX" :  4,
    "AY" :  8,
    "AZ" :  3,
    "BX" :  1,
    "BY" :  5,
    "BZ" :  9,
    "CX" :  7,
    "CY" :  2,
    "CZ" :  6
}

interpret2 = {    ##Dictionary of all possible cases and their score equivalent
    "AX" :  3,
    "AY" :  4,
    "AZ" :  8,
    "BX" :  1,           ## X - LOSE // Y - DRAW // Z - WIN
    "BY" :  5,
    "BZ" :  9,
    "CX" :  2,
    "CY" :  6,
    "CZ" :  7 
}

def part1(text):
    for i in range(0, len(text)):           ##Assign dictionary value of list element to the element itself Problem 2
        text[i] = interpret[text[i]]

    print("The answer for part 1 is: ", sum(text))


def part2(text):
    for i in range(0, len(text)):           ##Assign dictionary value of list element to the element itself Problem 2
        text[i] = interpret2[text[i]]
        
    print("The answer for part 2 is: ",  sum(text))


part1(text)
part2(text2) 

        



