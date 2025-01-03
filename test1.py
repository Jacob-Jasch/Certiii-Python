#---------------------------------------------------------------- qustoin 1 if else print

y1 = 50
y2 = "50"
y3 = True
y4 = y1 == int(y2)

if(y3 == y4):
 print(type(y4))

if(str(y1) == y2):
   print("Yes, y1 and y2 have the same value")
else:
   print("No, y1 and y2 do not have the same value")

#---------------------------------------------------------------- qustoin 2 data types

x1 = 90
x2 = 36.21
x3 = "Monday"
x4 = False


x5 = str(x1) + str(x2) + x3 + str(x4)
print(x5)

#---------------------------------------------------------------- qustoin 3 letter's number value 

z1 = "TAFE"
z2 = "tafe"

if (z1 < z2):
  print("z1 is smaller then z2")

#---------------------------------------------------------------- qustoin 4 conpair nummbers

x1 = 50

#if x1 is less then 60 print "x1 is less then 40"
#if x1 is greater then 20 print "x1 is greater then 40"
#else print "x1 is between 20 and 60"

if(x1 < 60):
  print("x1 is less then 60")
if(x1 > 20):
  print("x1 is greater then 20")
else:
  print("x1 is between 20 and 60")

#---------------------------------------------------------------- qustoin 5 conpairing data types

t1 = "Hello"

#if t1 is int type, print "t1 is int", 
#else if t1 is float type, print "t1 is float",
#else if t1 is string type, print "t1 is string"
#else print "i don't know"

t1Type = type(t1)

if(t1Type == int):
  print("t1 is int")
elif(t1Type == float):
  print("t1 is float")
elif(t1Type == str):
  print("t1 is string")
else:
  print("i don't know")

#---------------------------------------------------------------- qustoin 6 conpair nummbers

a = 14
b = 27
#if both a & b are even numbeers, print "both a & b are even numbers"
#if both a & b are odd numbers, print "both a & b are odd numbers"
#if a & b are NOT both even or odd numbers, find out which one is even, which is odd
#if a is an odd, print "a is a odd numbeer, and the remainder is" + a's remander, else print "a is an even number"
#if b is an odd, print "b is an odd number, and the reimader is" + b's remainder else print "b is an even number"

if(a % 2 == 0 and b % 2 == 0):
  print("both a & b are even number's")
elif(a % 2 != 0 and b % 2 != 0):
    print("both a & b are odd number's")
elif(a % 2 == 0 and b % 2 != 0 or a % 2 != 0 and b % 2 == 0):
  if(a % 2 !=0):
    print("a is an odd number and a's reimander is " +str(a % 2))
  else:
    print("a as an even number")
  if(b % 2 !=0):
    print("b is an odd number and b's reimander is " +str(b % 2))
  else:
    print("b is an even number")
#---------------------------------------------------------------- qustoin 7 (aka homework) say range of number
#x = "\u0033\u0039"
x = input("Enter number here (in console )")

if(int(x) <10):
  print("x is between 1 and 10")
elif(int(x) <20):
  print("x is between 11 and 20")
elif(int(x) <30):
  print("x is between 31 and 30")
elif(int(x) <40):
  print("x is between 31 and 40")
elif(int(x) <50):
  print("x is between 41 and 50")
elif(int(x) <60):
  print("x is between 51 and 60")
elif(int(x) <70):
  print("x is between 61 and 70")
elif(int(x) <80):
  print("x is between 71 and 80")
elif(int(x) <90):
  print("x is between 81 and 90")
elif(int(x) <100):
  print("x is between 91 and 100")
elif(int(x) >100):
  print("x is greater then 100")
#---------------------------------------------------------------- 
print("sample 1")
num = 0
while (num < 10):
  print(num)
  num += 1

for num in range(10):
  print(num)

print("sample 2")
for num in range(0,10,2):
  print(num)

num = 0
while (num <10):
  print(num)
  if(num ==8):
    break
  num += 1

#---------------------------------------------------------------- random

print("sample5")
import random
x = random.randint(1, 10)
for i in range (10):
  if(i > x):
    print(i, ">",x)
  elif(i == x):
    print(i, "=",x)
  elif(i < x):
    print(i, "<",x)
#---------------------------------------------------------------- qustoin 1    8/03/2022  conpair numbers
num = 1
while(num < 20):
  print(num)
  num += 2
for num in range(1,20,2):
  print(num)
#---------------------------------------------------------------- qustoin 2    8/03/2022
#x = "\u0033\u0039"
num1 = 1
num2 = 10

x = input("Enter number here (in console )")

while(True):
  if(int(num1) < int(x) < int(num2)):
    print("x is between " +str(num1) +" and " +str(num2))
  num1 += 10
  num2 += 10


x = input("Enter number here (in console )")
y = int(x)
r1 = 1
for num in range(1,11):
  for num2 in range(r1, r1 +10):
    if(y == num2):
      print("x is between " +str(r1) + " and " + str(r1 + 9))
  r1 = r1 + 10
#---------------------------------------------------------------- qustoin 3    8/03/2022
sum = 0
i = 0
while(i < 99):
   sum = sum + i
   i = i + 2
#---------------------------------------------------------------- homework
x = 8
for i in range(x + 1):
  print(i)
for j in range(x, -1, -1):
  print(j)

x = input("Enter nummber here")
for i in range(int(x)):
  print(i, end=" ")
for j in range(int(x), -1, -1):
  print(j, end=" ")

import random
x = random.randint(1, 10)
y = input("Please enter your number here ")
while(y.isdigit()):
  if (int(y) == x):
    print("Yes, the number is " + str(x))
  elif(int(y) < x):
    y = input("Ented number is less then random number, please try again ")
  elif(int(y) > x):
    y = input("Ented number is less then random number, please try again ")


import random
x = random.randint(1, 10)
y = input("Please enter your number here ")
guesscount = 0
while(y.isdigit()):
  if (int(y) == x):
    guesscount += 1
    print("Yes, the number is " + str(x))
  elif(int(y) < x):
    guesscount += 1
    y = input("Ented number is less then random number, please try again ")
  elif(int(y) > x):
    guesscount += 1
    y = input("Ented number is less then random number, please try again ")

strRows = input("How many rows do you want ")
rows = int(strRows)
for rownumber in range(1, rows, +1):
  for startnumber in range(1, rownumber +1):
    continue
  print("* " * startnumber)

strRows = input("How many rows do you want ")
rows = int(strRows)
for rownumber in range(1, rows, +1):
  for startnumber in range(1, rownumber +1):
    print("*", end=" ")
  print()

string = "wiofjwaaipjwfnoiawjpkdopfijnmjrp745"
lettercount = 0
LetterToBeCounted = input("Please enter the letters you want to be counted ")
for char in string:
  if(char != LetterToBeCounted):
    continue
  else:
    lettercount = lettercount + 1
print("Total number of " + LetterToBeCounted + " is:" + str(lettercount))

string = "HelloWorld"

for test in string:
  print(test)

#---------------------------------------------------------------- activity 2 15/03/2022 the sum of all odd numbers under 100

total = 0
for num in range(101):
  if(num % 2 == 0):
    continue
  total += num
print("The sum of odd numbers between 0-100 is" + str(total))

#---------------------------------------------------------------- activity 3 15/03/2022 
#in 0-1000,
#count the numbers that % 3 = 0, print the count numbers;
#count the numbers that % 5 = 0, print the count numbers;
#count the numbers that %3 & % 5 = 0, print the count numbers;
x = 3
y = 5
TotalThreeCount = 0
TotalFiveCount = 0
TotalBothCount = 0

for num in range(1001):
  if(num % x == 0):
    TotalThreeCount += 1

  if(num % y == 0):
    TotalFiveCount += 1
  
  if(num % y == 0):
    if(num % x == 0):
      TotalBothCount += 1
print("% 3: " + str(TotalThreeCount) + "\n" + "%5: "  + str(TotalFiveCount))
print("% 3 & 5: " + str(TotalBothCount) )
#---------------------------------------------------------------- prints the number of letters in "total count"

TotalCount = 0

for num in range(1, 101):
  if(num % (2 * 3 * 5) == 0):
    TotalCount += 1
    print(str(num) + " %2 & %3 & %5 is 0")
print("the count number of %2 & %3 & %5 is " + str(TotalCount))

#---------------------------------------------------------------- prints the number of letters in string

string = "Hello World! I am your boss!"
space = " "
CounterWSpace = 0
CounterNSpace = 0

for test in string:
  CounterWSpace += 1
  if (test != " "):
    CounterNSpace += 1
print(CounterNSpace)
print(CounterWSpace)

#does the same thing as each other

print(len(string))
print(len(string.replace(" ","")))

#---------------------------------------------------------------- 22/03/2022 list

thislist = ["apple", "banna", "cherry", "apple", "cherry"]
#print(len(thislist))

for x in thislist:
  print(x)

for y in range(len(thislist)):
  print(thislist[y])

#---------------------------------------------------------------- 22/03/2022 conbine list

student1 = ["Travis", 21, "male", True]
student2 = ["Masket", 22, "male", True]
student3 = ["Selena", 23, "female", True]
student4 = ["Phillp", 24, "male", True]

for x in range(len(student2)):
  student1.append(student2[x])
print(student1)

#---------------------------------------------------------------- 22/03/2022 remove from list

student1 = ["Travis", 21, "male", True]
student2 = ["Masket", 22, "male", True]
student3 = ["Selena", 23, "female", True]
student4 = ["Phillp", 24, "male", True]

for x in range(len(student2)):
  student1.append(student2[x])
print(student1)

student1.remove(student1[4])
print(student1)

#---------------------------------------------------------------- 22/03/2022 print set spot in list

list1 = ["q", "w", "a", "s", "z", "x"]
print(list1[4])

#---------------------------------------------------------------- 22/03/2022 sort list

list1 = ["q", "w", "a", "s", "z", "x"]
list1.sort()
print(list1)

#---------------------------------------------------------------- 22/03/2022 print list without the [ ] , and keep all in same line

list1 = ["q", "w", "a", "s", "z", "x"]

for x in range(len(list1)):
  print(list1[x], end=" ")

#---------------------------------------------------------------- 22/03/2022 Tuple(a list that can not change)

tuple1 = ["name", "age", "gender", "in class"]
list2 = ["Ross", 30, "male", True]
print(tuple1)
print(list2)

#---------------------------------------------------------------- 22/03/2022 def

def sum(num1,num2):
  num3 = num1 + num2 
  print(num3)

x = int(input("Enter number here (in console) "))
y = int(input("Enter number here (in console) "))

sum(x,y)




# create a functoin to display "Hello" name, "you are the best!"
# functoin need to have arguments of name
# input name useing input()

def display(e1):
  print("Hello " + e1 + ", you are probebly not a puppy")

name = input("Enter your name here (in console) ")
display(name)
#---------------------------------------------------------------- 22/03/2022 calcorlater

# create a functoin to do calcatltosin for 2 numbers
# in the functoin you nead 3 agurments, num 1, num2, operator(+, -, *, /, **)

# create a functoin to do calcatltosin for 2 numbers
# in the functoin you nead 3 agurments, num 1, num2, operator(+, -, *, /, **)

def sum():
  num1,z,num2 = int(input("Enter first number here (in console) ")), (input("Enter the operator (+, -, *, /, **) here ")), int(input("Enter last number here (in console) "))  
  if(z == "+"):
    print(str(num1) + " " + z + " " + str(num2) + " = " +str(num1 + num2))
  elif(z == "-"):
    print(str(num1) + " " + z + " " + str(num2) + " = " +str(num1 - num2))
  elif(z == "*"):
    print(str(num1) + " " + z + " " + str(num2) + " = " +str(num1 * num2))
  elif(z == "**"):
    print(str(num1) + " " + z + " " + str(num2) + " = " +str(num1 ** num2))
  elif(z == "/"):
    if(num2 != 0):
      print(str(num1) + " " + z + " " + str(num2) + " = " +str(num1 / num2))
    else:
      while(z == "/" and num2 == 0):
        print("you can not divide by 0")
        sum()
  else:
    print("'explodes!'")


sum()

#----------------------------------------------------------------