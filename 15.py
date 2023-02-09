'''15.Dictionary
1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
1.1. Adding the values in dictionary
1.2. Updating the values in dictionary
1.3. Accessing the value in dictionary
1.4. Create a nested loop dictionary
1.5. Access the values of nested loop dictionary
1.6. Print the keys present in a particular dictionary
1.7. Delete a value from a dictionary
1.1. Creating a Dictionary with at least 5 key value pairs of the Student ID and Name:'''


student_dict = {1001: "John Doe", 1002: "Jane Doe", 1003: "Jim Brown", 1004: "Jill Smith", 1005: "Jack Ryan"}
#1.2. Updating the values in dictionary:


student_dict[1001] = "John Smith"

#1.3. Accessing the value in dictionary:

print(student_dict[1001]) # Output: John Smith

#1.4. Creating a nested loop dictionary:


student_subjects = {1001: {"Math": 89, "Science": 92, "English": 95},
                    1002: {"Math": 80, "Science": 84, "English": 82},
                    1003: {"Math": 75, "Science": 72, "English": 78},
                    1004: {"Math": 90, "Science": 92, "English": 88},
                    1005: {"Math": 82, "Science": 86, "English": 80}}

#1.5. Accessing the values of nested loop dictionary:

print(student_subjects[1001]["Math"]) # Output: 89

#1.6. Printing the keys present in a particular dictionary:


print(student_dict.keys()) # Output: [1001, 1002, 1003, 1004, 1005]

#1.7. Deleting a value from a dictionary:

del student_dict[1001]