def print_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord("A") + j) + " ", end="")
        print("\n")


print_pattern(5)
