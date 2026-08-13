####Option1
# days={
# "monday": {
#     "morning": "Have a delicious breakfast!", 
#     "afternoon": "Work on that Python course!", 
#     "evening": "It's gym time!"
#     },
# "tuesday": {
#     "morning": "Go for a morning walk!", 
#     "afternoon": "Have you done your laundry and cooking, yet?", 
#     "evening": "Relaxation time!"
#     },
# "wednesday": {
#     "morning": "Read a book!", 
#     "afternoon": "Study dictionaries in Python!", 
#     "evening": "How about a run outside?"
#     },
# "thursday": {
#     "morning": "Study German for 30 min!", 
#     "afternoon": "Doctor's appointment at 3 pm!", 
#     "evening": "Relaxation time!"
#     },
# "friday": {
#     "morning": "Watch a video in Spanish!", 
#     "afternoon": "Make a video on your gym progress!", 
#     "evening": "Calisthenics: pull ups and pistol squats!"
#     },
#     }

# while True:
#     day_user=input("What day is it? ").lower().strip()
    
#     if day_user not in days:
#         print ("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday, Thursday, Friday")
#     elif day_user in days:
#         break
# while True:
#     time_user=input("What time of day? ").lower().strip()
#     if time_user not in days.get(day_user):
#         print ("Sorry, I don't recognize your message. Try: morning, afternoon, evening")
#     elif time_user in days.get(day_user):
#         break

# data_acc=days[day_user][time_user]
# print (data_acc)

##########################Option 2


# days={
#     "monday": {
#       "morning": "Have a delicious breakfast!", 
#       "afternoon": "Work on that Python course!", 
#       "evening": "It's gym time!"
#       },
#     "tuesday": {
#       "morning": "Go for a morning walk!", 
#       "afternoon": "Have you done your laundry and cooking, yet?", 
#       "evening": "Relaxation time!"
#       },
#     "wednesday": {
#       "morning": "Read a book!", 
#       "afternoon": "Study dictionaries in Python!", 
#       "evening": "How about a run outside?"
#       },
#     "thursday": {
#       "morning": "Study German for 30 min!", 
#       "afternoon": "Doctor's appointment at 3 pm!", 
#       "evening": "Relaxation time!"
#       },
#     "friday": {
#       "morning": "Watch a video in Spanish!", 
#       "afternoon": "Make a video on your gym progress!", 
#       "evening": "Calisthenics: pull ups and pistol squats!"
#       },
#       }

# def validate_input(user_input):
#         if not user_input:
#             print ("Not input")
#             return None
#         cleaned=user_input.strip().lower()

#         abbreviations={
#             "mon": "monday",
#             "tue": "tuesday",
#             "wed": "wednesday",
#             "thu": "thursday",
#             "fri": "friday",
#         }
#         if cleaned in abbreviations:
#             return abbreviations[cleaned]
#         else:
#             return cleaned


# while True:
#     day_user=input("What day is it? (q for quit)")
#     if day_user=="quit" or day_user=="q":
#         break
#     time_user=input("What time of day? (q for quit) ")
#     if time_user=="quit" or time_user=="q":
#         break

#     result_day=validate_input(day_user)
#     result_time=validate_input(time_user)

#     print (days.get(result_day, {}).get(result_time))


################Option 3
days = {
    "monday": {
        "morning": {
            "suggestion": "Have a delicious breakfast!",
            "metadata": {
                "duration": "20 min",
                "location": "kitchen",
                "energy_level": "low"
            }
        },
        "afternoon": {
            "suggestion": "Work on that Python course!",
            "metadata": {
                "duration": "2 hours",
                "location": "home",
                "energy_level": "medium"
            }
        },
        "evening": {
            "suggestion": "It's gym time!",
            "metadata": {
                "duration": "1 hour",
                "location": "gym",
                "energy_level": "high"
            }
        }
    },
    "tuesday": {
        "morning": {
            "suggestion": "Go for a morning walk!",
            "metadata": {
                "duration": "30 min",
                "location": "park",
                "energy_level": "medium"
            }
        },
        "afternoon": {
            "suggestion": "Have you done your laundry and cooking, yet?",
            "metadata": {
                "duration": "1.5 hours",
                "location": "home",
                "energy_level": "medium"
            }
        },
        "evening": {
            "suggestion": "Relaxation time!",
            "metadata": {
                "duration": "2 hours",
                "location": "living room",
                "energy_level": "low"
            }
        }
    },
    "wednesday": {
        "morning": {
            "suggestion": "Read a book!",
            "metadata": {
                "duration": "45 min",
                "location": "balcony",
                "energy_level": "low"
            }
        },
        "afternoon": {
            "suggestion": "Study dictionaries in Python!",
            "metadata": {
                "duration": "1.5 hours",
                "location": "home",
                "energy_level": "medium"
            }
        },
        "evening": {
            "suggestion": "How about a run outside?",
            "metadata": {
                "duration": "40 min",
                "location": "neighborhood",
                "energy_level": "high"
            }
        }
    },
    "thursday": {
        "morning": {
            "suggestion": "Study German for 30 min!",
            "metadata": {
                "duration": "30 min",
                "location": "bedroom",
                "energy_level": "medium"
            }
        },
        "afternoon": {
            "suggestion": "Doctor's appointment at 3 pm!",
            "metadata": {
                "duration": "1 hour",
                "location": "clinic",
                "energy_level": "low"
            }
        },
        "evening": {
            "suggestion": "Relaxation time!",
            "metadata": {
                "duration": "2 hours",
                "location": "living room",
                "energy_level": "low"
            }
        }
    },
    "friday": {
        "morning": {
            "suggestion": "Watch a video in Spanish!",
            "metadata": {
                "duration": "25 min",
                "location": "bedroom",
                "energy_level": "low"
            }
        },
        "afternoon": {
            "suggestion": "Make a video on your gym progress!",
            "metadata": {
                "duration": "1 hour",
                "location": "home - desk",
                "energy_level": "medium"
            }
        },
        "evening": {
            "suggestion": "Calisthenics: pull ups and pistol squats!",
            "metadata": {
                "duration": "45 min",
                "location": "Planet Fitness",
                "energy_level": "high"
            }
        }
    }
}
# import os
import json
FILE_PATH="config.json"
DEFAULT_DATA=days

def start_pr():
    try:
        with open(FILE_PATH, "r") as file:
            print ("Loading existing JSON file...")
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print ("File not found. Creating a new file!")
        with open (FILE_PATH, "w") as file:
            print ("Adding you data...")
            json.dump(DEFAULT_DATA, file, indent=4)
            return DEFAULT_DATA

data=start_pr()


def validate_input(user_input):
    if not user_input:
        print ("Try again! Non-input")
        return None
    cleaned=user_input.lower().strip()
    abbreviations={
            "mon": "monday",
            "tue": "tuesday",
            "wed": "wednesday",
            "thu": "thursday",
            "fri": "friday",
        }
    if cleaned in abbreviations:
        upd_cleaned=abbreviations[cleaned]
        return upd_cleaned
    else:
        return cleaned

def dict_check(to_check_day, to_check_time):
    if to_check_day in DEFAULT_DATA and to_check_time in DEFAULT_DATA[to_check_day]:
        return DEFAULT_DATA[to_check_day][to_check_time]["suggestion"]
    else:
        return "Not found"


def positive ():
    print (f'\nDuration: {DEFAULT_DATA[revised_day][revised_time]["metadata"]["duration"]}\nLocation: {DEFAULT_DATA[revised_day][revised_time]["metadata"]["location"]}\nEnergy level: {DEFAULT_DATA[revised_day][revised_time]["metadata"]["energy_level"]}\n')

def quitting():
    print ("Quitting...")

def negative():
    return None

def default_action():
    print ("Not recognized. Try again (Y/N/q) ")
    return "Invalid"

actions = {
        "yes": positive, 
        "y": positive,
        "no": negative,
        'n': negative,
        "q": quitting,
        "quit": quitting
    }
 
#check default_action
def selected_function(input_yes_no):
    return actions.get(input_yes_no, default_action)

def output_check(result, meta_data):
    if result!="Not found":
        # meta_user=input("Do you want to see more info? Y/N/q: ").lower().strip()
        answer_function=selected_function(meta_data)
        return answer_function()
    else:
        return None

while True:
    day_user=input("What day is it? (q for quit) ")
    # day_user="mon"
    if day_user=="q":
        break
    time_user=input("What time of day? (q for quit) ")
    # time_user="evening"
    if time_user=="q":
        break
    revised_day=validate_input(day_user)
    revised_time=validate_input(time_user)
    output=dict_check(revised_day, revised_time)
    print (output)
    while True:
        meta_user=input("Do you want to see more info? Y/N/q: ").lower().strip()
        if meta_user not in ["yes", 'no', 'y', 'n', 'q', 'quit']:
            print (default_action())
        else: 
            break
    upd_result=output_check (output, meta_user)
    if meta_user=="q":
        break
        
    

    