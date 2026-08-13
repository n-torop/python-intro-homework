user=int(input("Enter a number: "))
sign=''
num=''

if user<0:
    sign='negative'
elif user==0:
    sign='zero'
else:
    sign="positive"

if user%2==1:
    num="odd"
elif user%2==0:
    num="even"


print (f'{user} is {sign}.')
print (f'{user} is {num}.')