def part_one():
    input = open('input.txt', 'r')
    vals = []
    depth = 0
    horizontal = 0
    for val in input:
        line = val.strip().split()
        if line[0] == 'up':
            depth -= int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        else:
            horizontal += int(line[1])
    print(f"Part One: {depth*horizontal}")
## Correct Answer: 1451208

def part_two():
    input = open('input.txt', 'r')
    vals = []
    depth = 0
    horizontal = 0
    aim = 0
    for val in input:
        line = val.strip().split()
        if line[0] == 'up':
            aim -= int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        else:
            horizontal += int(line[1])
            adder = (aim*int(line[1]))
            depth += adder
    print(f"Part Two: {depth*horizontal}")
## Correct Answer: 1620141160

if __name__ == "__main__":
    part_one()
    part_two()