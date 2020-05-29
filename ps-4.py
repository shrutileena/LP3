a = int(input())
b = int(input())
resa = list()
resb = list()
count = 0

for i in range(1, a+1):
    if a % i == 0:
        resa.append(i)

for j in range(1, b+1):
    if b % j == 0:
        resb.append(j)

for k in range(len(resa)):
    for m in range(len(resb)):
        if (resa[k] == resb[m]):
            count = count + 1

print(count)