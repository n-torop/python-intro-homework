while True:
    user_input=input("Enter a number: ")
    try:
        user_input=float(user_input)
        print (f"You entered: {user_input}")
        break
    except ValueError:
        print ("That's not a valid number. Try again.")