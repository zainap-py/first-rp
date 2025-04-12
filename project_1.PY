#Python calculator

operator = input("choose operator + - * / ")

num1 = float(input('enter first number: '))
num2 = float(input('enter second number: '))

if operator == '+':
    result = num1 + num2
    print(round(result,2))
elif operator == '-':
    result = num1 - num2
    print(round(result,2))
elif operator == '*':
    result = num1 * num2
    print(round(result,2))
elif operator == '/':
    result = num1 / num2
    print(round(result,2))
else:
    print(f'{operator} is not a valid operator')
