import operator

classes = (('V',1), ('VI',1), ('V',2), ('VI',2), ('VI',3), ('VII',1))
Counter = dict()

for Class in classes:
    if Class[0] not in Counter:
        Counter[Class[0]] = 1
    else:
        Counter[Class[0]] = Counter[Class[0]] + 1

sorted_counter = dict(sorted(Counter.items(), key = operator.itemgetter(1), reverse=True))
print(sorted_counter)