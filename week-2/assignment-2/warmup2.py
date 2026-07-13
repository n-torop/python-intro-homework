# Navigation commands I used:

# pwd 
# ls 
# cd python-intro-homework
# touch warmup2.py
# mv /Users/natalia/Documents/CTD/python_homework/python-intro-homework /Users/natalia/Documents/CTD/python_homework/python-intro-homework/week-2/assignment-2


what_date=input ("What is today's date (Format Month, day, year)? ")
print (f'You said today is {what_date}.')

#compare the current date with input
listt=what_date.split(",")
print ("1", listt)
upd=[]
for el in listt:
    new=el.strip()
    upd.append(new)

from datetime import date
now=date.today()

month=now.strftime("%B")
day=now.strftime('%d')
year=now.strftime('%Y')
date_list=[month, day, year]

def check (listt, date_list):
    for item in upd:
        if item in date_list:
            print (f'{item} is correct')
        else:
            print (f'{item} is incorrect')
            return "The date is wrong!"        

check(upd, date_list)
