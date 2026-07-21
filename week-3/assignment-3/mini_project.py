#####Option1
days={
'monday': {
    'morning': 'Have a delicious breakfast!', 
    'day': 'Work on that Python course!', 
    'evening': "It's gym time!"
    },
'tuesday': {
    'morning': 'Go for a morning walk!', 
    'day': 'Have you done your laundry and cooking, yet?', 
    'evening': "Relaxation time!"
    },
'wednesday': {
    'morning': 'Read a book!', 
    'day': 'Study dictionaries in Python!', 
    'evening': "How about a run outside?"
    },
'thursday': {
    'morning': 'Study German for 30 min!', 
    'day': "Doctor's appointment at 3 pm!", 
    'evening': "Relaxation time!"
    },
'friday': {
    'morning': 'Watch a video in Spanish!', 
    'day': "Make a video on your gym progress!", 
    'evening': "Calisthnics: pull ups and pistol squats!"
    },
    }

while True:
    day_user=input("What day is it? ").lower().strip()
    if day_user not in days:
        print ("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday, Thursday, Friday")
    if day_user in days:
        break
time_user=input("What time of day? ").lower().strip()

data_acc=days[day_user][time_user]
print (data_acc)

##########################Option 2

# day_user=input("What day is it? ")
# time_user=input("What time of day? ")


# days={
#     'monday': {
#       'morning': 'Have a delicious breakfast!', 
#       'day': 'Work on that Python course!', 
#       'evening': "It's gym time!"
#       },
#     'tuesday': {
#       'morning': 'Go for a morning walk!', 
#       'day': 'Have you done your laundry and cooking, yet?', 
#       'evening': "Relaxation time!"
#       },
#     'wednesday': {
#       'morning': 'Read a book!', 
#       'day': 'Study dictionaries in Python!', 
#       'evening': "How about a run outside?"
#       },
#     'thursday': {
#       'morning': 'Study German for 30 min!', 
#       'day': "Doctor's appointment at 3 pm!", 
#       'evening': "Relaxation time!"
#       },
#     'friday': {
#       'morning': 'Watch a video in Spanish!', 
#       'day': "Make a video on your gym progress!", 
#       'evening': "Calisthnics: pull ups and pistol squats!"
#       },
#       }

# def validate_input(user_input):
#     if not user_input:
#         print ("Not input")
#         return None
#     cleaned=user_input.strip().lower()

#     abbreviations={
#         "mon": 'monday',
#         "tue": 'tuesday',
#         'wed': 'wednesday',
#         'thu': 'thursday',
#         'fri': 'friday',
#     }
#     if cleaned in abbreviations:
#         return abbreviations[cleaned]
#     else:
#         return cleaned


# result_day=validate_input(day_user)
# result_time=validate_input(time_user)

# print (days.get(result_day, {}).get(result_time))
