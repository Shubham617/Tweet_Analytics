testlist = [1, 2, 3, 5, 9, 10, 256, -3]

result = list(filter(lambda x: x%3==0, map(lambda x: -1*x, testlist)))

print(result.__str__())