def print_pattern(n):
    char = "A"
    for i in range(n):
        for j in range(i + 1):
            print(char + " ", end="")
        char = chr(ord(char) + 1)
        print("\n")


print_pattern(5)
