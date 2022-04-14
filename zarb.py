s = int(input())
h = int(input())

for row in range(1, s+1):
    print()
    for col in range(1, h+1):
        print(col * row, end="\t")