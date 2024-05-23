def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(ord("A") + j) + " ", end="")
        print("\n")


print_pattern(5)
