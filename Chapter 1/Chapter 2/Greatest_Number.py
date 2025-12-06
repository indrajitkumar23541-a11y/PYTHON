a = int(input("Enter Number a : "))
b = int(input("Enter Number b : "))
c = int(input("Enter Number c : "))
if(a>b and a>c):
    print("Greatest Number = ",a)
elif(a<b and b>c):
    print("Greatest Number = ",b)
else:
    print("Greatest Number = ",c)