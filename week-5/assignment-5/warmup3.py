names=['Alisa', 'Berta', 'Cinthia', 'Alisson', 'Valorie']
index=-1

user=input('Enter a name to search for: ')
for n in range (len(names)):
    if names[n]==user:
        index=n
        break
if index!=-1:
    print (f'Found {user} at index {index}.')
else:
    print (f'"{user}" was not found in the list.')

