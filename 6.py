'''6.Strings
1. Different ways creating a string
2. Concatenating two strings using + operator
3. Finding the length of the string
4. Extract a string using Substring
5. Searching in strings using index()
6. Matching a String Against a Regular Expression With matches()
7. Comparing strings
8. startsWith(), endsWith() and compareTo()
9. Trimming strings with strip()
10. Replacing characters in strings with replace()
11. Splitting strings with split()
12. Converting integer objects to Strings
13. Converting to uppercase and lowercase'''

#There are several ways to create a string in Python:

#Using single quotes:

str = 'Hello World'
#Using double quotes:

str = "Hello World"
#Using triple quotes:

str = """Hello World"""
#Using the str() function:

str = str(42)
#To concatenate two strings, you can use the + operator:
str1 = "Hello" 
str2 = " World" 
str3 = str1 + str2

#To find the length of a string, you can use the len() function:
str = "Hello World" 
length = len(str)

#To extract a substring from a string, you can use slicing:
str = "Hello World" 
sub_string = str[0:5]

#To search for a substring in a string, you can use the in keyword:
str = "Hello World" 
if "o" in str:
 print("Found")

#To match a string against a regular expression, you can use the re module:
import re
str = "Hello World"
match = re.search("[A-Z][a-z]+", str)

#To compare two strings, you can use the == operator:
str1 = "Hello" 
str2 = "Hello" 
is_equal = str1 == str2

#To check if a string starts with a certain prefix, you can use the startswith() method. To check if a string ends with a certain suffix, you can use the endswith() method. To compare two strings lexicographically, you can use the <, >, and <=, >= operators:
str = "Hello World"
starts_with_h = str.startswith("H") 
ends_with_w = str.endswith("W") 
comparison = str < "Hello"

#To trim a string, you can use the strip() method:
str = " Hello World " 
trimmed = str.strip()

#To replace characters in a string, you can use the replace() method:
str = "Hello World" 
replaced = str.replace("o", "a")

#To split a string into a list of substrings, you can use the split() method:
str = "Hello,World" 
sub_strings = str.split(",")

#To convert an integer to a string, you can use the str() function:
num = 42 
str = str(num)


#convert a string to uppercase, you can use the upper() method. To convert a string to lowercase, you can use the lower() method:
str = "Hello World" 
upper = str.upper()
lower = str.lower()