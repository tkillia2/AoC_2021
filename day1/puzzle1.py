input = open('puzzle1.txt', 'r')
vals = []
for val in input:
    val = val.strip()
    vals.append(int(val))
increasing = 0
for val in range(1,len(vals)):
    if vals[val] > vals[val-1]:
        increasing += 1
print(increasing)
## Correct Answer: 1559

