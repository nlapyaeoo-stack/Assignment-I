num1=int(input("Give a 1st num :"))
num2=int(input("Give a 2nd num :"))
all_num1=id(num1)
print("Allocation of num1",all_num1)
hex_num2=hex(num2)
print("Hexitation of num2",hex_num2)
num3=num1+num2
print("Addition:",num3)

if num1>num2:
    num4=num1-num2
    print("Substraction:",num4)
    num5=num1//num2
    print("Division:",num5)
elif num2<num1:
    num4=num2-num1
    print("Substraction:",num4)
    num5=num2//num1
    print("Division:",num5)
 
all_num3=id(num3)
print("Allocation of num3:",all_num3) 
hex_num3=hex(num3)
print("Haxitation of num3:",hex_num3)
all_num4=id(num4)
print("Allocation of num4:",all_num4)
hex_num4=hex(num4)
print("Hexitation of num4:",hex_num4)
all_num5=id(num5)
print("Allocation of num5:",all_num5)
hex_num5=hex(num5)
print("Hexitation if num5:",hex_num5)
    