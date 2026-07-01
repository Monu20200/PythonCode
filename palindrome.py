#Palindrome
l=[]
while True:
    val= input("enter a value: ")
    l.append(val)
    a = input("would you like to continue? (y/n): ")
    if a in "nN":
        break
print(l)
l2= l.copy()
l2.reverse()
print(l2)
if l == l2:
    print("palindrome")
else:        
    print("not palindrome")