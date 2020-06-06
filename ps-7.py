num = int(input("Enter no of lines: "))
Lines = list()

for i in range(num):
    Lines.append(input())

for Line in Lines:
    if 'not' in Line:
        if 'poor' in Line:
            if 'poor' > 'not':
                print(Line.replace("not that poor", "good"))
            else:
                print(Line)
        else:
            print(Line)
    else:
        print(Line)

