def is_valid_score(score):
    if score>=0 and score<=100:
        return True
    elif score<0 or score>100:
        return False

    
try:
    user=int(input("Type your score (0-100): "))
except ValueError:
    print ("Not an integer.")
    user=int(input("Type your score (0-100): "))


ans=is_valid_score(user)
if ans:
    print ("Valid score.")
else:
    print ("Invalid score — must be between 0 and 100.")