# Ans. 8.a
try:
    print("Program to divide two numbers")
    num1 = float(input("Enter first number:- "))
    num2 = float(input("Enter firs number:- "))
    result = num1 / num2
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Division by Zero")

print("")

# Ans. b
try:
    print("Program to convert a string to an integer")
    S = input("Enter number:- ")
    Convert_into_int = int(S)
    print(f"Converting string {S} into integer {Convert_into_int}")
except ValueError:
    print("Error: Value Error")

print("")

# Ans. c
try:
    print("Program to access an element in a list")
    lst = list(input("Give a list(eg.- 123456):- "))
    print(lst)
    index = int(input("Enter a element which you want to access:- "))
    elememt = lst[index]
    print(f"The element is {elememt}")
except IndexError:
    print("Error: Index out of range. please enter valid index")

except ValueError:
    print("Error: Invalid input.Please enter valid integer ")

print("")

# Ans.  d.
try:
    print("Program to divide two numbers")
    num1 = float(input("Enter first number:- "))
    num2 = float(input("Enter firs number:- "))
    result = num1 / num2
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Division by Zero")

print("")

# Ans.  e.
try:
    print("Program to divide two numbers")
    num1 = float(input("Enter first number:- "))
    num2 = float(input("Enter firs number:- "))
    result = num1 / num2
    print(f"The result is {result}")

except Exception as e:
    print("An error occurred", str(e))
