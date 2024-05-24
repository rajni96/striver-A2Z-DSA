def reverse_numbers(nums):
    count = 0
    reverse = 0
    while nums:
        r = nums % 10
        reverse = reverse * 10 + r
        nums = nums // 10

    return reverse


numbers = 32257
output = reverse_numbers(numbers)
print(output)
