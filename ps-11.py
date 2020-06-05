n = int(input("Enter length of list: "))
inputLst = list()

for i in range(n):
    inputLst.append(int(input()))
#inputLst = [14,46,43,27,57,41,45,21,70]
print(inputLst)

for i in range(len(inputLst)):
    min_index = i
    for j in range(i+1, len(inputLst)):
        if (inputLst[min_index] > inputLst[j]):
            min_index = j

    inputLst[i], inputLst[min_index] = inputLst[min_index], inputLst[i]

print(inputLst)