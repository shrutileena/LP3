n = int(input())
words = list()
a = dict()
count = 0

for i in range(n):
    words.append(input())

for word in words:
    a[word] = a.get(word, 0) + 1

print(len(a))
for key, value in a.items():
    print(a[key], end=" ")