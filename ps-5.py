word = input()
newWord = str()

for i in word:
    if i not in newWord:
        newWord = newWord + i
    else:
        continue

print(newWord)