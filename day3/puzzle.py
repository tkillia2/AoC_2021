def part_one():
    input = open('input.txt', 'r')
    filelines = input.readlines()
    gamma = [0]*12
    ones = 0
    for val in filelines:
        line = val.strip()
        for l in range(0, len(line)):
            if line[l] == '1':
                gamma[l] += 1
    epsilon = [0]*12
    for v in range(0, len(gamma)):
        if gamma[v] > len(filelines)/2:
            gamma[v] = 1
            epsilon[v] = 0
        else:
            gamma[v] = 0
            epsilon[v] = 1
    gammas = int(''.join(str(l) for l in gamma), 2)
    epsilons = int(''.join(str(l) for l in epsilon), 2)
    print(f"Part One: {gammas*epsilons}")
# Correct Answer: 841526

def part_two():
    input = open('input.txt', 'r')
    filelines = input.readlines()
    vals = []
    ones = 0
    one = []
    zero = []
    i = 0
    vals2 = []
    for val in filelines:
        line = val.strip()
        vals.append(line)
        vals2.append(line)
    while i <= 11:
        for val in vals:
            if val[i] == '1':
                ones += 1
                one.append(val)
            else:
                zero.append(val)
        if ones >= len(vals)/2:
            vals = one.copy()
        else:
            vals = zero.copy()
        ones = 0
        one = []
        zero = []
        i += 1
    oxy_gen = int(''.join(str(l) for l in vals), 2)
    i = 0
    one = []
    zero = []
    while i <= 11:
        for val in vals2:
            if val[i] == '1':
                ones += 1
                one.append(val)
            elif val[i] == '0':
                zero.append(val)
        if ones < len(vals2)/2:
            vals2 = one.copy()
        else:
            vals2 = zero.copy()
        ones = 0
        one = []
        zero = []
        i += 1
        if len(vals2) == 1:
            break
    co2 = int(''.join(str(l) for l in vals2), 2)
    print(f"Part Two: {oxy_gen * co2}")
# Correct Answer: 4790390

if __name__ == "__main__":
    part_one()
    part_two()