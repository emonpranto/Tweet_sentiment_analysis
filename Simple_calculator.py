def Calculator(num1,num2,operator):
    if operator == '+':
        answer = int(num1)+int(num2)
    if operator == '-':
        answer=int(num1)-int(num2)
    if operator == '*':
        answer=int(num1)*int(num2)
    if operator == '/':
        answer=int(num1)/int(num2)
    return print(answer)

Calculator(2,3,'/')