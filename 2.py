"""2.Operators
1. Write a function for arithmetic operators(+,-,*,/)
2. Write a method for increment and decrement operators(++, --)
3. Write a program to find the two numbers equal or not.
4. Program for relational operators (<,<==, >, >==)
5. Print the smaller and larger number"""


def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    else:
        return 0


result = arithmetic_operation(1, 4, '+')
print("result", result)


def operator(a, operator):
    if operator == '+':
        a = a+1
    elif operator == '-':
        a = a-1
    else:
        return 0
    return a


result = operator(5, '-')
print("Result", result)


def equal(a, b):
    if a == b:
        print('Equal')
    else:
        print("Not equal")


equal(1, 1)


def relational_operation(a, b, operator):
    if operator == '<':
        return a < b
    elif operator == '<=':
        return a <= b
    elif operator == '>':
        return a > b
    elif operator == '>=':
        return a >= b
    else:
        return 0


result = relational_operation(1, 4, '>')
print("result", result)


def minmax(arr):
    min = arr[0]
    max = arr[0]


def minmax(arr):

    min = arr[0]
    max = arr[0]

    for num in arr:
        if num < min:
            min = num
        if num > max:
            max = num
    print("Smallest number", min)
    print("Largest number", max)


arr = [2, 5, 8, 9, 6]
minmax(arr)


def min_max():
    # Get the input array from the user
    arr = list(map(int, input(
        "Enter the numbers in the array, separated by spaces: ").strip().split()))

    # Assign the first element of the array as the initial minimum and maximum number
    min_num = arr[0]
    max_num = arr[0]

    # Loop through the array and compare each number with the minimum and maximum number
    for num in arr:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    # Print the minimum and maximum number
    print("Smaller number:", min_num)
    print("Larger number:", max_num)
