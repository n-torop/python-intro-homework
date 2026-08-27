numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def menu():
    print ("=== Number Cruncher === \n1. Find minimum\n2. Find maximum\n3. Search for a number\n4. Sort the list\n5. Quit")


def find_min(data):
    smaller=data[0]
    counter=0
    for el in data:
        try: 
            if smaller>data[counter+1]:
                smaller=data[counter+1]
            counter+=1
        except IndexError:
            break
    print(smaller)
    return smaller

def find_max(data):
    bigger=data[0]
    counter=0
    for el in data:
        try: 
            if bigger<data[counter+1]:
                bigger=data[counter+1]
            counter+=1
        except IndexError:
            break
    print(bigger)
    return bigger

def search(data, user):
    found=False
    for i in range(len(data)):
        new_i=i
        if data[i]==user:
            print (new_i)
            found=True
    if found==False:   
        print ("-1")

def sorting (data):
    copy=data.copy()
    n=len(copy)
    for i in range(n-1):
        for m in range (n-i-1):
            if copy[m]>copy[m+1]:
                copy[m], copy[m+1]=copy[m+1], copy[m]
    print (copy)
    return copy

def quitting(): 
    print ("Goodbye!")



def main ():
    while True:
        menu()
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
    

if __name__=="__main__":
    main()