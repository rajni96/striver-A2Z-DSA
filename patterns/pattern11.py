def print_pattern(n):
    for i in range(n):
        start = 1
        if i % 2 == 0:
            start = 0
        for j in range(i + 1):
            start = 1 - start
            print(start, end=" ")
        print("\n")


print_pattern(5)
