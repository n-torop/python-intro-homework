import csv, os
from datetime import datetime

path="../data/expenses.csv"


if os.path.exists(path):
    print ("found")
    with open (path, 'r') as file:
        records=list(csv.DictReader(file))
        

    for item in records:
        item['amount']=float(item['amount'])
    # print (records)

    food=[item for item in records if item['category'] == 'Food']
    total=sum (item['amount'] for item in food)
    # print (total)

    with open ('food_report.txt', 'w') as report:
        now=datetime.now()
        report.write (f"Food Expense Report — generated {now.strftime('%B %d, %Y')}\n")
        for item in food:
            report.write (f"{item['date']}: ${item['amount']:.2f}\n")
            
        report.write (f"Total: ${total:.2f}\n")
    


else:
    print ("Error. File doesn't exist!")


