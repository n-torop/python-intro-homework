
def open_file(file_name):
    with open (file_name, 'r') as file:
        count=1
        for line in file:
            print(f'Line {count}: {line.strip()}')
            count+=1



user_file_name='../data/notes.txt'
open_file(user_file_name)