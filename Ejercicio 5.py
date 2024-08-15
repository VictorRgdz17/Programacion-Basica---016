def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def multip_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
print(sum_list([1, 2, 3, 4]))
print(multip_list([1, 2, 3, 4]))