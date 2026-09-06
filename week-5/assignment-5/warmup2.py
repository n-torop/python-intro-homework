non_int="That's not a positive integer. Try again."

while True:
    user=input('Enter a positive integer: ')
    try:
        user=int(user)
        if user<=0:
            print(non_int)
        elif user>0:
            print (f"Got it: {user}")
            break
        

    except:
        print (non_int)
   