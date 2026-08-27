import csv
class ValueMissing(Exception):
    pass

def collect_messy_data(path):
    
    clean_list_dict=[]
    messy_list_dict=[]

    try:
        with open (path, "r") as p:
            reader=csv.DictReader(p)
            for index, row in enumerate(reader, start=1):
                if None in row:
                    messy_list_dict.append (f"Row {index}: extra column detected — skipped")
                    continue

                try:
                    name=row["name"]
                    category=row["category"]
                    amount_val=row["amount"]
                    
                    dict_item={"name": name,
                               "category": category,
                               "amount": amount_val}
                    
                    try:
                        amount=float(dict_item["amount"])
                        clean_list_dict.append(dict_item)
                      
                    except ValueError:
                        
                        messy_list_dict.append(f"Row {index}: ValueError — could not convert '{dict_item["amount"]}' to float.")

                        if amount=="" or name=="" or category=="":
                            print ("empty")
                            messy_list_dict.append(f"Row {index}: An expected column is missing from a row.")
                    except KeyError:
                        if name==None or category==None or amount==None:
                            messy_list_dict.append(f"Row {index}: extra column detected — skipped")
                except ValueError:
                        messy_list_dict.append(f"Row {index}: ValueError — could not convert '{amount}' to float.")

                        if amount=="" or name=="" or category=="":
                            messy_list_dict.append(f"Row {index}: An expected column is missing from a row.")
                except KeyError:
                    if name==None or category==None or amount==None:
                        messy_list_dict.append(f"Row {index}: extra column detected — skipped")

                        



    except FileNotFoundError:
        print("An error. File not found.")
        return 
    return clean_list_dict, messy_list_dict


path_name="../data/messy_data.csv"


clean_list_dict, messy_list_dict=collect_messy_data(path_name)

def report(clean, messy):
    attempted_rows=len(clean)+len(messy)
    print ("=== CSV Report ===")
    print (f"Rows attempted:  {attempted_rows}")
    print (f"Rows parsed:     {len(clean)}")
    print (f"Rows skipped:    {len(messy)}")
    print ("\nSkipped rows:")
    for el in messy:
        print (f"  {el}")
    print ("Clean data:")
    for item in clean:
        print (f"{item["name"]} | {item["category"]} | ${item["amount"]}")

report(clean_list_dict, messy_list_dict)

collect_messy_data(path_name)

