from string import ascii_letters
import os
os.chdir(r'C:\Users\Thatcher\Desktop\Coding Stuff\Advent of Code\Day 3')

with open("Day3input.txt") as file:
    text = file.read().split()


finalSum = 0

for ele in text:     
    half = len(ele) // 2
    l = set(ele[:half])
    r = set(ele[half:])
    
    for i, n in enumerate(ascii_letters):
        if n in l and n in r:
            finalSum += i + 1

print("The answer to part 1 is:", finalSum)

##-----------------------Part 2--------------------------##
finalSum = 0
j = 3
for i in range(0, len(text), 3):
    bags = text[i:j]
    j += 3
    
    for i, n in enumerate(ascii_letters):
        if n in bags[0] and n in bags[1] and n in bags[2]: 
            finalSum += i + 1

print("Answer to part 2 is:", finalSum)
