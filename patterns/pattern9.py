def print_pattern(n):
    for i in range(0, n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        for j in range(n - i - 1):
            print(" ", end="")

        print("\n")
    for i in range(n - 1, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        for j in range(n - i - 1):
            print(" ", end="")

        print("\n")


print_pattern(5)
