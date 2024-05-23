def print_pattern(n):
    for i in range(n, 0, -1):
        char = chr(ord("A") + i - 1)
        for j in range(n - i + 1):
            print(chr(ord(char) + j)+" ", end="")

        print("\n")


print_pattern(5)
