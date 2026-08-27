
def file_reader(path):
    try:
        with open (path, "r") as p:
            print ("File exists.")
            content=p.read()
    except FileNotFoundError:
        print(f'Error: "{path}" was not found. Please check the file path and try again.')
        return ""


path_name= "../data/missing.txt"
file_reader(path_name)
