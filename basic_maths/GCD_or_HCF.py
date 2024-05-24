# def find_gcd(num1, num2):
#     if num1 == 0 or num2 == 0:
#         return max(num1, num2)
#     else:
#         if num1 > num2:
#             num1 = num1 - num2
#         else:
#             num2 = num2 - num1
#         return find_gcd(num1, num2)


def find_gcd(num1, num2):
    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return max(num1, num2)


num1 = 81
num2 = 18
output = find_gcd(num1, num2)
print(output)
