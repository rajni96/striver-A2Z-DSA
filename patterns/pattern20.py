def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        for l in range(n - i):
            print(" ", end="")
        for l in range(n - i):
            print(" ", end="")
        for j in range(i, 0, -1):
            print("*", end="")
        print("\n")
    for i in range(n - 1, 0, -1):
        for j in range(i, 0, -1):
            print("*", end="")
        for l in range(n - i):
            print(" ", end="")
        for l in range(n - i):
            print(" ", end="")
        for j in range(i, 0, -1):
            print("*", end="")
        print("\n")


print_pattern(5)
