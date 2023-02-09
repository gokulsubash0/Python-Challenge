'''3.Loops
1. Write a program to print “Bright IT Career” ten times using for loop
2. Write a program to print 1 to 20 numbers using the while loop.
3. Program to equal operator and not equal operators
4. Write a program to print the odd and even numbers.
5. Write a program to print largest number among three numbers.
6. Write a program to print even number between 10 and 20 using while
7. Write a program to print 1 to 10 using the do-while loop statement.
8. Write a program to find Armstrong number or not
9. Write a program to find the prime or not.
10. Write a program to palindrome or not.
11. Program to check whether a number is EVEN or ODD using switch
12. Print gender(Male/Female) program according to given M/F using switch'''


for i in range(0,10):
 print("Bright IT Career")




i=1
while(i<21):
 print(i)
 i=i+1



a=int(input("Enter a number"))
b=int(input("Enter 2nd number"))

if a==b:
    print("Equal")
elif a!=b:
    print("Not equal")    




a=int(input("Enter a number"))

if a%2==0:
    print("Even")
else: print('Odd')


for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")




a=3
b=4
c=1

largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
print("Largest",largest)


i=10
while(i<21):
    print(i)
    i=i+2
    

i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

    i=1
while True:
    print(i)
    i+=1
    if i >10:
     break

num = 153
original_num = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10

if original_num == sum:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")


num = 29
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

 

word = "level"
reversed_word = word[::-1]


if word == reversed_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


num = 7

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


gender = 'M'

if gender == 'M':
    print("Male")
elif gender == 'F':
    print("Female")
else:
    print("Invalid Gender")




