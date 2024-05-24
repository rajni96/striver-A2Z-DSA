import math


def check_prime(num):

    if num < 2:
        return True

    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False

    return True


# number = 32257
# output = check_prime(number)
# print(output)

# Test the function
numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 23, 25, 29, 31]
for number in numbers:
    print(f"{number} is prime: {check_prime(number)}")
