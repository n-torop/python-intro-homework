# 1. Traceback (most recent call last):
#   File "/Users/natalia/Documents/CTD/python_homework/python-intro-homework/week-2/assignment-2/warmup4.py", line 13, in <module>
#     upd=el+num
#         ~~^~~~
# TypeError: can only concatenate str (not "int") to str

#2. Error message was caused by cancatenating a string and an integer
#3. fixed it by printing the number near a letter without cancatenation

variable1=input("Type a word: ")
num=0
for el in variable1:
    upd=el
    print (upd, num)
    num+=1