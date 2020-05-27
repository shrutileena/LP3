classes = (('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1))
counts = dict()

from div in classes :
    counts[div] = counts.get(div, 0) + 1

print(counts)