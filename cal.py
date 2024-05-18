a=eval(input("Enter 1st number:"))
b=eval(input("Enter 2nd number:"))
print('''1. Add(+)
2. Substrate (-)
3. Multiply(*)
4. Divide(÷)
5. Exit''')
c=input("Enter operator:")

print("---------------------------------")
if c=="1":
    print(a+b)
elif c=="2":
    print(a-b)
elif c=="3":
    print(a*b)    
elif c=="4":
    print(a/b)
elif c=="5":
    print("Thanks")
else:
    print("wrong operator selected")      
        
    