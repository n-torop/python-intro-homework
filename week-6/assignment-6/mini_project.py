numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def show_menu():
    print ("=== Number Cruncher === \n1. Find minimum\n2. Find maximum\n3. Search for a number\n4. Sort the list\n5. Quit")
    user_choice=input("Choose an option (1-5): ")
    print (user_choice)
    return user_choice


def find_min(data):
    min_val=numbers[0]
    for num in data:
        if num<min_val:
            min_val=num
    return min_val

def find_max(data):
    max_val=numbers[0]
    for num in data:
        if num>max_val:
            max_val=num
    return max_val

def search(data, user):
    found=False
    for i in range(len(data)):
        if data[i]==user:
            found=True
            return i
    if found==False:   
        return -1
    

def bubble_sort (data):
    copy=data.copy()
    n=len(copy)
    for i in range(n-1):
        for m in range (n-i-1):
            if copy[m]>copy[m+1]:
                copy[m], copy[m+1]=copy[m+1], copy[m]
    return copy

def quitting(): 
    print ("Goodbye!")

def main ():
    while True:
        user_input=show_menu()
        if user_input=="1":
            min_val=find_min (numbers)
            print (min_val)
        elif user_input=="2":
            find_max (numbers)
            max_val=find_max (numbers)
            print (max_val)
        elif user_input=="3":
            value=int(input("Enter number to search: "))
            result=search (numbers, value)
            if result<0:
                print ("Not found")
            elif result>=0:
                print (f"Found at index {result}")

        elif user_input=="4":
            print (bubble_sort (numbers))
            
        elif user_input=="5":
            quitting()
            break
    

if __name__=="__main__":
    main()