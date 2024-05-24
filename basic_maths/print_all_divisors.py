import math

divisors = []


def find_divisors(num):
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if num / i != i:
                divisors.append(int(num / i))

    return sorted(divisors)


number = 12
output = find_divisors(number)
print(output)
