def check_armstrong_Number(num):
    count = 0
    armstrong = 0
    actual_num = num
    power = len(str(num))
    while num:
        r = num % 10
        armstrong = armstrong + r**power
        num = num // 10

    return armstrong == actual_num


number = 153  # 371
output = check_armstrong_Number(number)
print(output)
