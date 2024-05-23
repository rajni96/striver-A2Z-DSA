def print_pattern(n):
    for i in range(1, 2 * n):
        star = i
        if i > n:
            star = 2 * n - i
        for j in range(star):
            print("*", end="")

        print("\n")


print_pattern(5)
