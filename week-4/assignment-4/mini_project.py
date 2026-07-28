students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_score=0
current_score=int
num=0
name=str

total=0
calc=len(students)

new_set=set()
high_scorers=[]

for el in students:
    for key, value in el.items():
       
        if key=="score":
            current_score=students[num]["score"]

            total+=current_score
            if current_score>75:
                high_scorers.append(students[num]["name"])

            if top_score<current_score:
                top_score=current_score
                name=students[num]['name']
            num+=1

        if key=="subject":
            new_set.add(value)
        

average=total/calc

print (f'Top scorer: {name} ({top_score})')

print (f'Class average: {average}')
print (f'Subjects offered: {new_set}')
print (f'High scorers: {high_scorers}')


