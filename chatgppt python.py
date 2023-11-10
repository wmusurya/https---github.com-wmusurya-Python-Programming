#Basic input and output

name=input("enter your name")
age=int(input(" enter your age")) 

name='surya'
age=25
print(f'my name is {name} and my age is {age}')


age=int(input("enter your age "))

print(f"In 10 years youll be {age+10}")


# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F


grade = int(input("Enter your grade: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 60 and grade < 70:
    print('D')
elif grade >= 0 and grade < 60:
    print("You have failed")
else:
    print("Invalid grade. Grade should be between 0 and 100.")

number=int(input("enter a number"))

if number % 2== 0:
    print("it is even")
else:
    print("It is odd")


year=int(input("year"))

if year%4==0:
    print("correct")
else:
    print("incorrect")


# leap year
year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

colors=['Red','Green','Yellow']
color=input("enter the color from above: ")



if color =='Red':
    print("STOP")
elif color =='Green':
    print("GO")
elif color =='yellow':
    print("HOLD")

else:
    print("wrong color")







traffic_light=['red','yellow','green']
current_color=input("enter the above color")

if current_color not in traffic_light:
    print("sorry the color is not there")

else:
    current_index=traffic_light.index(current_color)
    next_index=(current_index+1)%3
    next_color=traffic_light['next color is',next_color]

numbers = [x for x in range(9, 90) if x % 9 == 0]

number = input('Enter the input: ')

try:
    number = int(number)  # Convert input to an integer

    if number not in numbers:
        print("The number given is not present in the list.")
    else:
        current_index = numbers.index(number)
        next_index = (current_index + 1) % len(numbers)
        next_number = numbers[next_index]
        print("The next number is", next_number)
except ValueError:
    print("Invalid input. Please enter a valid number.")


# While Loop

count=0
while count<=5:
    print(count)
    count=count+1

count=0
while count<=10:
    print(count)
    count=count+1





password='python123'
user_input=input("enter the password")

while user_input!=password:
    print("the password is worng")
    user_input=input("enter the password")

print("Correct Password")



sum=0
num=1

while num<5:
    sum=sum+num
    num=num+1

print(sum)

number=list(range(1,10))
number


correct_number=8
number=int(input("enter a number "))

while number!=correct_number:
    print('incorrect number')
    number=int(input("enter a number"))

print("correct number")


# For Loop

fruits=['apple','mango','orange']
for i in fruits:
    print(i)

# Common Loop Patterns

for i in range(5):
    print(i)

# looping through string

a="python"

for i in a:
    print(i,end=' ')



for i in range(10):
    if i==3:
        break
    elif i==7:
        continue
    print(i)

for i in range(1,10):
    if i%2==0:
        print(f"{i :} even")
    else:
        print(f"{i :} odd")

number = 9
mult = 10

while mult < 10:
    mult = mult * 9
    number = number + 1

print(f"Final number: {number}")


number=9
count=1

while count<=10:
    result=count*number
    print(result)
    count=count+1


a=9

for i in range(0,11):
    print(i*a)

a=[x for x in range(0,66) if x%6==0]
a


a=8

fact=1
for i in range(1,a+1):
    fact=fact*i

print(fact)


