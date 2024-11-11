def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 *num2
def div(num1,num2):
    return num1/num2

print("SELECT AN OPERATOR\n")
print("1- addition")
print("2- Subration")
print("3- multiplication")
print("4- division")

select = int(input("Select a num from 1 2 3 4:"))
first_number = int(input("Enter ur first number:"))
second_number = int(input("enter ur second number"))


if select == 1:
    print(first_number,"+",second_number ,"=",add(first_number,second_number))
elif select ==2:
    print(first_number,"-" ,second_number, "=",sub(first_number,second_number))
elif select ==3:
    print(first_number,"*",second_number ,"=",mul(first_number,second_number))
elif select ==4:
    print(first_number,"/",second_number, "=",div(first_number,second_number))
else:
    print("invalid input ")