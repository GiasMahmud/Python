"""
print("Hello World")
# Arithmstic Operator
Banana = 5;
Ruti = 10;
Total = Banana + Ruti
Banana = 10;
print (Total);
Total = Banana ** Ruti
print (Total);
# conditional Statement
marks = 35
marks = input ("Enter Your number: ")
marks = int(marks)
"""

# Calculate grade system
"""
if marks >= 80:
    print("GPA: A+")
elif marks >= 70:
    print("GPA: A")
elif marks >= 60:
    print("GPA: A-")
elif marks >= 50:
    print("GPA: B")
elif marks >= 40:
    print("GPA: C")
elif marks >= 80:
    print("GPA: C")
else:
    print("GPA: F")
    """
#Check even or odd
"""
n = input("Enter Your Number: ")
n = int(n)

if n % 2 == 0:
    print(n, " Is Even")
else:
    print(n, " Is Odd") 
"""
#Check Positive or Negative
"""
n = input("Enter Your Number: ")
n = int(n)

if n >= 0:
    if n % 2 == 0:
        print(n, " Is Positive and Even Number")
    else:
        print(n, " Is Positive and Odd Number")
else:
    if n % 2 == 0:
        print(n, " Is Negative and Even Number")
    else:
        print(n, " Is Negative and Odd Number")
"""
# Uses of AND operator
"""
n = input("Enter Your Number: ")
n = int(n)

if n >= 0 and n % 2 == 0:
        print(n, " Is Positive and Even Number")
elif n >= 0 and n % 2 == 1:
        print(n, " Is Positive and Odd Number")
elif n <= 0 and n % 2 == 0:
        print(n, " Is Negative and Even Number")
else:
        print(n, " Is Negative and Odd Number")
        """

# Uses of OR operator
"""
n = input("Enter Your Number: ")
n = int(n)

if n >= 0 or n % 2 == 0:
        print(n, " Is True")
elif n >= 0 or n % 2 == 1:
        print(n, " Is false")
elif n <= 0 or n % 2 == 0:
        print(n, " Is false")
else:
        print(n, " Is false")
        """
      
# find Leaf year

year = input("Enter the year: ")
year = int(year)

if year % 100 == 0 and year % 400 == 0:
    print(year, "Is leaf year")
elif year % 4 == 0 and  year % 100 != 0:
    print(year, "Is leaf year")
else:
    print(year, "is not leaf year")