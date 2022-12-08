### PART 1 ###
'''
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of
cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to
quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

For the first few pairs, this list means:
-Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned 
sections 6-8 (sections 6, 7, 8).
-The Elves in the second pair were each assigned two sections.
-The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of 
section assignments look like this:
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully 
contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner 
will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?
'''
import os

pwd = os.getcwd()
input_folder = pwd + '\input\\'

#with open(input_folder + 'input_test.txt', 'r') as file:
with open(input_folder + 'day4_input.txt', 'r') as file:
    data = file.read().strip()

lines = data.split('\n')

inc = 0

for i in lines:
    split_line = i.split(',')
    s1 = split_line[0]
    s2 = split_line[1]

    split_sec1 = s1.split('-')
    split_sec2 = s2.split('-')
    s1_min = int(split_sec1[0])
    s1_max = int(split_sec1[1])
    s2_min = int(split_sec2[0])
    s2_max = int(split_sec2[1])
    
    if (s1_min >= s2_min and s1_max <= s2_max) or (s1_min <= s2_min and s1_max >= s2_max):
        #print('yes: ' + i)
        inc += 1
    else:
        #print('no: ' + i)
        continue
print(inc)
  
### PART 2 ###
'''
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) 
do overlap:
5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''

inc = 0

for i in lines:
    split_line = i.split(',')
    s1 = split_line[0]
    s2 = split_line[1]

    split_sec1 = s1.split('-')
    split_sec2 = s2.split('-')
    s1_min = int(split_sec1[0])
    s1_max = int(split_sec1[1])
    s2_min = int(split_sec2[0])
    s2_max = int(split_sec2[1])
    
    range1 = range(s1_min, s1_max+1)
    range2 = range(s2_min, s2_max+1)

    if s1_min in range2 or s1_max in range2 or s2_min in range1 or s2_max in range1:
        #print('yes: ' + i)
        inc += 1
    else:
        #print('no: ' + i)
        continue
print(inc)


