size = int(input())


for x in range(1, size + 1):
    for y in range(0, x):
        print('*', end="")
    print()
for x in range(size - 1, 0, -1):
    for y in range(0, x):
        print('*', end="")
    print()