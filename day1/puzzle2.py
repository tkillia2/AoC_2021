input = open('puzzle1.txt', 'r')
vals = []
for val in input:
    val = val.strip()
    vals.append(int(val))
increasing = 0
A = list(vals[0:3])
for val in range(1,len(vals)):
    B = list(vals[val:val+3])
    if(len(B) < 3):
        break
    elif sum(B) > sum(A):
        increasing += 1
    A = B
print(increasing)
# Correct Answer: 1600

