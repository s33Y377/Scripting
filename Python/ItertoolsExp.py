import itertools

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(itertools.accumulate(data, max)))
