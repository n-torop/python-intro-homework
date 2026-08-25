import csv

def read_csv(file):
    with open(file, 'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            
            print (f"{row['name']}: {row['score']}")


path='../data/students.csv'

read_csv(path)
