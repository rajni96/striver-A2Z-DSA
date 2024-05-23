def print_pattern(n):
    for i in range(n):
        char = "A"
        for j in range(n - i - 1):
            print("  ", end="")
        for k in range(i + 1):
            print(char + " ", end="")
            char = chr(ord(char) + 1)
        char = chr(ord(char) - 1)
        for l in range(i):
            char = chr(ord(char) - 1)
            print(char + " ", end="")
        for m in range(n - i - 1):
            print("  ", end="")
        print("\n")


print_pattern(4)
