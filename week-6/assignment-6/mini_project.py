numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def menu():
    print ("=== Number Cruncher === \n1. Find minimum\n2. Find maximum\n3. Search for a number\n4. Sort the list\n5. Quit")


def find_min(data):
    min_val=numbers[0]
    for num in data:
        if num<min_val:
            min_val=num
    print (min_val)
    return min_val

def find_max(data):
    max_val=numbers[0]
    for num in data:
        if num>max_val:
            max_val=num
    print (max_val)
    return max_val

def search(data, user):
    found=False
    for i in range(len(data)):
        if data[i]==user:
            print(i)
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