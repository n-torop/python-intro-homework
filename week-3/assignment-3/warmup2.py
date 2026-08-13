user_input=int(input("How old are you: "))
category=''

if user_input>=0 and user_input<=12:
    category='Child'
elif user_input>=13 and user_input<=17:
    category='Teen'
elif user_input>=18 and user_input<=64:
    category='Adult'
elif user_input>=65:
    category="Senior"

if category=='Child' or category=='Teen'or category=="Senior":
    print (f'You are a {category}.')
else:
    print (f'You are an {category}.')
