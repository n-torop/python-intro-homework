import csv

def read_csv(file):
    with open(file, 'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            
            print (f'{row['name']}: {row['score']}')


path='/Users/natalia/Documents/CTD/python_homework/python-intro-homework/week-7/data/students.csv'

read_csv(path)
