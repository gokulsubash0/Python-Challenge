#Arrays

#Function to add integer values of an array
def add_array_values(arr):
    return sum(arr)

#Function to calculate the average value of an array of integers
def average_of_array(arr):
    return sum(arr) / len(arr)

#Program to find the index of an array element:

def find_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return -1

#Function to test if array contains a specific value:

def contains_value(arr, value):
    return value in arr

#Function to remove a specific element from an array:

def remove_element(arr, value):
    arr.remove(value)
    return arr

#Function to copy an array to another array:

def copy_array(arr):
    return arr[:]

#Function to insert an element at a specific position in the array:

def insert_element(arr, value, index):
    arr.insert(index, value)
    return arr

#Function to find the minimum and maximum value of an array:

def min_max_of_array(arr):
    return min(arr), max(arr)

#Function to reverse an array of integer values:

def reverse_array(arr):
    return arr[::-1]

#Function to find the duplicate values of an array:

def find_duplicates(arr):
    return [item for item, count in collections.Counter(arr).items() if count > 1]

#Program to find the common values between two arrays:

def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

#Method to remove duplicate elements from an array:

def remove_duplicates(arr):
    return list(set(arr))
# set(arr) function creates a set from the list arr. A set is a collection of unique elements, so any duplicates in the original list are automatically removed.
#list(...) function then converts the set back into a list. This creates a new list with the same unique elements as the original set

#Method to find the second largest number in an array:

def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

#Method to find the second largest number in an array:

def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

#Method to find number of even number and odd numbers in an array:

def even_odd_count(arr):
    even_count = 0
    odd_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

#Function to get the difference of largest and smallest value:

def difference(arr):
    return max(arr) - min(arr)

# Method to verify if the array contains two specified elements (12, 23):

def contains_elements(arr, value1, value2):
    return (value1 in arr) and (value2 in arr)

# Program to remove the duplicate elements and return the new array:

def remove_duplicates(arr):
    return list(set(arr))
