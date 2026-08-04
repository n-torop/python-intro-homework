numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def menu():
    print ("=== Number Cruncher === \n1. Find minimum\n2. Find maximum\n3. Search for a number\n4. Sort the list\n5. Quit")


def find_min(data):
    ordered=sorted(data)
    print (ordered[0])
    return ordered[0]

def find_max(data):
    ordered=sorted(data)
    for i in ordered[::-1]:
        print (i)
        break

def search(data, user):
    found=False
    for i in range(len(data)):
        new_i=i
        if data[i]==user:
            print (new_i)
            found=True
    if found==False:   
        print ("not found")

def sorting (data):
    n=len(data)
    for i in range(n-1):
        for m in range (n-i-1):
            if data[m]>data[m+1]:
                data[m], data[m+1]=data[m+1], data[m]
    print (data)

def quitting(): 
    print ("Goodbye!")

menu()
while True:
    
    user_input=input("Choose an option (1-5): ")
    if user_input=="1":
        find_min (numbers)
    elif user_input=="2":
        find_max (numbers)
    elif user_input=="3":
        value=int(input("Enter number to search: "))
        search (numbers, value)
    elif user_input=="4":
        sorting (numbers)
    elif user_input=="5":
        quitting()
        break
   

