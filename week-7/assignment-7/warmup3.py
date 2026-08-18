import os

print (os.getcwd())
file="data/expenses.csv"
if os.path.exists (file):
    print ('expenses.csv found.')
else:
    print ("expenses.csv not found.")

path=os.path.join("data", "expenses.cvs")
print(path)