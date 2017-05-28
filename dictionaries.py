
# Dictionaries #
	#Utilizes key-value pairs

student = {'name': 'Kyrie', 'age': 24, 5: 'Numbers', 'courses':['Welding', 'Physics']}

print(student)
print(student['name'])
print(student['courses'])
print(student[5])

	#Can add and edit individual key-value pairs
student['Mobile'] = '678-8906'
student['name'] = 'Daria'
print(student)

	#Can edit multiple parts of dictionary
student.update({'age': 28, 'Mobile': '000-0000'})
print(student)

#print(student('Mobile')) Key doesn't exist, so error
print(student.get('Mobile', 'Unknown')) #Used to avoid error from nonexistent key
							#2nd argument can be message if key doesn't exist, other None is printed


	#Delete/remove attributes
del student[5]
age = student.pop('age')
print(student)
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items()) #Prints key and value pairs

for key in student: #Only prints keys
	print(key)



for key, value in student.items(): # Prints both together
	print(key, value)



