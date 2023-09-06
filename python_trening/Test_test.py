

count = 0
def count_positive_numbers(numbers):
    global count
    for num in numbers:
        if num > 0:
            count += 1

my_list = [1, -2, 3, -4, 5]
count_positive_numbers(my_list)
print(count)


def count_positive_numbers(numbers):
    positive_count = 0
    for num in numbers:
        if num > 0:
            positive_count += 1
    print(f'Количество положительных чисел: {positive_count}')
numbers = [1, -2, 3, 0, -4]
count_positive_numbers(numbers)