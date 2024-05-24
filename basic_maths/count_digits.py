# def count_digits(nums):
#     count = 0
#     for num in str(nums):
#         count += 1

#     return count


def count_digits(nums):
    count = 0
    while nums:
        count += 1
        nums = nums // 10

    return count


numbers = 1678945
output = count_digits(numbers)
print(output)
