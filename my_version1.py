#Calculator

print("--- Welcome to python Calculator --- ")
num1 = float(input("please enter first number: "))
num2 = float(input("please enter second number: "))
print('-- please choose operator -- ')
operator = input("+ - * / ")

if operator == "+":
    result = num1 + num2
    print(round(result,2))
elif operator == '-':
    result = num1 - num2
    print(round(result,2))
elif operator == "*":
    result = num1*num2
    print(round(result,2))
elif operator == "/":
    result = num1 / num2
    print(round(result,2))
else:
    print("Please Enter a valid operator")    
    

