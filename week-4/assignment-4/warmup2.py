student={
    'name': 'Emily',
    'grade': 90,
    'subjects': ['English', "Math", "Chemistry"],
    
}

for key, value in student.items():
    print (f'{key}: {value}')


student['graduated']=False
print (student)