num = int(input("enter the no to find factorial: "))
factorial = 1 
# for i in range(1,num+1):
#     factorial *=i 
i = 1
while i <= num:
    factorial *=i
    i+=1
print("the factorial of",num,"is",factorial)