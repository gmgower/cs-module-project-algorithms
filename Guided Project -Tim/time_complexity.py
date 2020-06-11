# https://youtu.be/uDY_XAJe0AE

def fun1(arr):
    x = arr[0]

    arr[0] *= 2

    for i in range(10):
        arr[i] *= 5

    for element in arr:
        print(element)

    return arr

# O(1 + 1 + 10 + n + 1)
# O(13 + n)
# O(n)

def fun1b(arr):
    x = arr[0]

    arr[0] *= 2

    for i in range(10):
        arr[i] *= 5

    return arr

# O(13) -> O(1)

def fun2(arr):
    extra_array = range(10)

    for i in range(len(arr)):
        for x in extra_array:
            arr[i] *= x
    
    return arr

# O(1 + (n * 10 * 1) + 1)
# O(2 + 10n)
# O(10n)
# O(n)

def fun2b(arr):
    extra_array = range(10)

    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i] *= arr[j]
    
    return arr

# O(1 + (n * n * 1) + 1)
# O(2 + 1n ** 2)
# O(n**2)

def what_if_I_pop(arr):
    x = arr.pop()

    return arr

# [0, 1, 2, 3, 4, 5]
# [1, 2, 3, 4]
# x = 0

# [0, 1, 2, 3, 4]

# What will pop/append do to time complexity?
## They're constant time operations!


# input: a long, unsorted array of numbers
def sort_me(arr):
    x = arr.pop()

    arr[1] *= 99

    arr.sort()

    return arr

# O(1 + 1 + (n log n) + 1)
# O( n log n)

def whats_in_the_box(arr):
    if 42 in arr:
        return "the meaning of life"

# O(n)


def power_of_2(num):
    exponent = 0
    while num > 1:
        num = num // 2
        exponent += 1

    return exponent

print(power_of_2(16))
print(power_of_2(32))





# space complexity
## range

def fun4(arr):
    new_arr = []

    for item in arr:
        new_arr.append(item)

    return new_arr

my_array = [1, 2, 3, 4]
# O(n) space complexity

def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)

# time complexity: O(n)
# space complexity: O(n)
