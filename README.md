# advent_of_code_18
https://adventofcode.com/2018

## Results

![alt text](results.png)

### Day 15 (revisited in 2021)
- Turns out my original algorithm was sound, the mistake for part 2 was to use binary search. It is possible to get no deaths
for, say, elf damage rate 13, but to have deaths for all the numbers lower and higher like 14, 15, 16, etc. This is because the
 positions and movements differ depending on the damage rate. E.g. for a high damage the elf might move towards a group of
 goblins sooner than if elf had a lower damage rate, so would get extra rounds of multiple damage from the group.
- Note, I rewrote the whole thing because I incorrectly thought the original was broken - the new one is much faster at least :)

## TODO

- Day 18 part 2 is super slow
- Day 19 work out what is going on
- Day 20
- Day 22 part 2
- Day 23 part 2
- Day 24 is slow

# TODO perhaps?
- Go through and tidy up as most solutions are confusing to follow
- Day 13 is a bit slow

