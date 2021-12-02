with open('inputD1.txt') as f:
    lines = f.readlines()

lines = list(map(int, lines))

''' Day 1 - part 1 '''

count = 0

for x in range(len(lines)-1) : 
    if lines[x+1] > lines[x] :
        count+=1

print(count)


''' Day 1 - part '2 '''

count = 0
a = 0
b = 0

for x in range(len(lines)-3) : 
    a = lines[x] + lines[x+1] + lines[x+2]
    b = lines[x+1] + lines[x+2] + lines[x+3]
    if a < b :
        count+=1

print(count)