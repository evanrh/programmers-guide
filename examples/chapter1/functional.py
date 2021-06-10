nums = [x for x in range(20)]
squares = list(map(lambda x: x * x, nums))
oddSquares = list(filter(lambda x: (x % 2) != 0, squares))
print(oddSquares)
