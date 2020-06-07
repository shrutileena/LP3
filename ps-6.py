import sys


def counting(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            print('-1')
            sys.exit(0)

    for i in arr:
        if i not in count:
            count.append(i)
        else:
            continue


m = int(input("Enter no of rows: "))
n = int(input("Enter no of columns: "))
b = []
count = []
min_rows = []
min_cols = []
max_rows = []
max_cols = []

for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input("Enter element: ")))
    b.append(a)

for i in range(m):
    min_index = 0
    max_index = 0
    for j in range(n-1):
        if b[i][j+1] < b[i][min_index]:
            min_index = j+1

        if b[i][j+1] > b[i][max_index]:
            max_index = j+1
    min_rows.append(b[i][min_index])
    max_rows.append(b[i][max_index])

for i in range(n):
    min_index = 0
    max_index = 0
    for j in range(m-1):
        if b[j + 1][i] < b[min_index][i]:
            min_index = j + 1

        if b[j + 1][i] > b[max_index][i]:
            max_index = j + 1
    min_cols.append(b[min_index][i])
    max_cols.append(b[max_index][i])

counting(min_rows)
counting(min_cols)
counting(max_rows)
counting(max_cols)

print(len(count))