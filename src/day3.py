### PART 1 ###
'''
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't 
quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did 
the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. 
Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each 
of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters 
represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw


-The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second 
compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
-The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
-The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
-The fourth rucksack's compartments only share item type v.
-The fifth rucksack's compartments only share item type t.
-The sixth rucksack's compartments only share item type s.

To help prioritize item rearrangement, every item type can be converted to a priority:
-Lowercase item types a through z have priorities 1 through 26.
-Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack 
is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
'''

#one letter per line is repeated in each half of string
#split string in half, find matching character
#from matching chars, find sum of char values

import os

pwd = os.getcwd()
input_folder = pwd + '\input\\'

#with open(input_folder + 'input_test.txt', 'r') as file:
with open(input_folder + 'day3_input.txt', 'r') as file:
    data = file.read().strip()

sacks = data.split('\n')

char_match = ''
result = 0

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
        'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
        'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30,
        'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40,
        'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50,
        'Y':51, 'Z':52
        }

for line in sacks:
    string_len = len(line.strip())
    half_len = int(string_len / 2)

    split1 = (line[:half_len])
    split2 = (line[(half_len):])

    for i in set(split1):
        if i in split2:
            char_match += i
#print(char_match)

for x in char_match:
    result += dict[x]     

print(result)

### PART 2 ###
'''
As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, 
within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, 
then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the 
rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by
finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above 
example, the first group's rucksacks are the first three lines:
-vJrwpWtwJgWrhcsFMMfFFhFp
-jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
-PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:
-wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
-ttgJtRGJQctTZtZT
-CrZsJsPPZsGzwwsLwLmpwMDw

In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, 
their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for
the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
'''

#elves in groups of 3 with same badge type carried
#one or more in group will only carry their group badge
#need to pull out all badges
#find the badge types for each group and sum total

char_match = ''
result = 0
i = 0

while i < len(sacks):
    sack1 = sacks[i]
    sack2 = sacks[i + 1]
    sack3 = sacks[i + 2]
    for item in sack1:
        if item in sack2 and item in sack3:
            char_match += item
            i += 3
            break

for x in char_match:
    result += dict[x]     

print(result)
