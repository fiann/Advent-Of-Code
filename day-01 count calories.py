# Count calories from lines of text
# See https://adventofcode.com/2022/day/1

elves = []
# Read text file and iterate over lines
with open("day-01-input.txt", "r") as file:
    elf = 0
    for line in file:
        line = line.rstrip()
        if line == "":
            elves.append(elf)
            elf = 0
        else:
            elf += int(line)

# Print the largest number in elves
print(f"Largest single elf: { max(elves) }")

# Print the sum of the three largest numbers in elves
elves.sort(reverse=True)
print(f"Sum of three largest elves: { elves[0] + elves[1] + elves[2] }")
