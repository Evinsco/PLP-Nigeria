print("Welcome to my online calculator")

print ("Enter first number")
first_var = int(input())

print("Enter operator")
operator = input()

print("second number")
Second_var = int(input())

 

if operator == "+":
    result = first_var + Second_var
    print(first_var, sign, Second_var, result)

elif operator == "-":
    result = first_var - Second_var
    print(first_var, sign, Second_var, result)

elif operator == "/":
    result = first_var / Second_var
    print(first_var, sign, Second_var, result)

elif operator == "*":
    result = first_var * Second_var
    print(first_var, sign, Second_var, result)

else:
    print("invalid syntax")