x = [i for i in range(5) if i%2 == 0]
print(x)

x = [[j for j in range(i)] for i in range(5)]
print(x)

x = [[x, y]for x, y in zip(range(5), range(5, 10))]
print(x)
