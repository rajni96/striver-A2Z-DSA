def print_pattern(n):
    number = 1
    for i in range(n):
        for j in range(i + 1):

            print(str(number) + " ", end="")
            number += 1

        print("\n")


print_pattern(5)
