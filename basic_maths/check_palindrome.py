def check_palindrome(nums):
    reverse = 0
    actual_nums = nums
    while nums:
        r = nums % 10
        reverse = reverse * 10 + r
        nums = nums // 10

    return reverse == actual_nums


numbers = 323
output = check_palindrome(numbers)
print(output)
