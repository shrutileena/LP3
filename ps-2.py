y = int(input("Enter year: "))

if len(str(y)) != 4:
    print("Wrong input! Enter again.")
else:
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                print(True)
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)
