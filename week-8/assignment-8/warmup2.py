while True:
    user_num=input("Enter the numerator: ")
    user_den=input("Enter the denominator: ")

    try:
        user_num=float(user_num)
        user_den=float(user_den)
        result=user_num/user_den
        print (f"{user_num} ÷ {user_den} = {result}")
        break
    except ZeroDivisionError:
        print ("Can't divide by zero — please try a non-zero denominator.")