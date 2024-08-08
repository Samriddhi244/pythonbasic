#simple 2 number calculator
def add(x,y):
    adding = x+y
    return adding;
def sub(x,y):
    if x>y:
        return x-y;
    else:
        return y-x;
def multiply(x,y):
    return x*y;
def divide(x,y):
    return x/y;

num1= float(input("enter any number"))
operator = input("enter the operator or operation ")
num2 = float(input("enter any number"))
if operator != '+' or operator != '-' or operator != '/' or operator != '*':
    print("please only give the mentioned operators '+','-' , '*' , '/' ")
    operator = input("enter valid operator")

#check the operators and operation specified and perform the operation for the numbers
if operator == '+':
    print("the addition of " , num1, "and" , num2 , "is" , add(num1,num2))
    num12 = num1+num2
    question = bool(input("do you want to operate another number?"))
    if question == True or question == 'yes':
        num3 = float(input("enter any number"))
        operator2 = input("enter the operator")
    else:
        print(add(num1,num2))
    if operator2 == operator:
        print(add(num12,num3))
    elif operator2 =='-':
        print(num12,"-",num3,"=",sub(num12,num3))
    elif operator2 == "*":
        print(num12,"*",num3,"=",multiply(num12,num3))
    elif operator2 =="/":
        print(num12,"/",num3,"=",divide(num12,num3))
if operator == '-' :
    print("the subtraction of " , num1, "and" , num2 , "is" , add(num1,num2))
    num12 = num1-num2
    question = bool(input("do you want to operate another number?"))
    if question == True or question == 'yes':
        num3 = float(input("enter any number"))
        operator2 = input("enter the operator")
    else:
        print(sub(num1,num2))
    if operator2 == operator:
        print(sub(num12,num3))
    elif operator2 =='+':
        print(num12,"+",num3,"=",add(num12,num3))
    elif operator2 == "*":
        print(num12,"*",num3,"=",multiply(num12,num3))
    elif operator2 =="/":
        print(num12,"/",num3,"=",divide(num12,num3))
if operator == '*' :
    print("the multiplication of " , num1, "and" , num2 , "is" , add(num1,num2))
    num12 = num1*num2
    question = bool(input("do you want to operate another number?"))
    if question == True or question == 'yes':
        num3 = float(input("enter any number"))
        operator2 = input("enter the operator")
    else:
        print(multiply(num1,num2))
    if operator2 == operator:
        print(multiply(num12,num3))
    elif operator2 =='-':
        print(num12,"-",num3,"=",sub(num12,num3))
    elif operator2 == "+":
        print(num12,"+",num3,"=",add(num12,num3))
    elif operator2 =="/":
        print(num12,"/",num3,"=",divide(num12,num3))
if operator == '/' :
    print("the division of " , num1, "and" , num2 , "is" , divide(num1,num2))
    num12 = num1+num2
    question = bool(input("do you want to operate another number?"))
    if question == True or question == 'yes':
        num3 = float(input("enter any number"))
        operator2 = input("enter the operator")
    else:
        print(divide(num1,num2))
    if operator2 == operator:
        print(divide(num12,num3))
    elif operator2 =='-':
        print(num12,"-",num3,"=",sub(num12,num3))
    elif operator2 == "*":
        print(num12,"*",num3,"=",multiply(num12,num3))
    elif operator2 =="+":
        print(num12,"+",num3,"=",add(num12,num3))
else:
    print("other complex opearation are not supported") 
