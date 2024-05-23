def print_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        for k in range(n - i - 1, 0, -1):
            print(" ", end="")
        for l in range(n - i - 1, 0, -1):
            print(" ", end="")
        for m in range(i + 1, 0, -1):
            print(m, end="")
            # i = i - m
        print("\n")


print_pattern(5)
