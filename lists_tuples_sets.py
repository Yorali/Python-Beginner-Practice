# Lists and tuples - sequential data
# Sets - Unordered collections with no duplicates


#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {} #INCORRECT. This is a dictionary
empty_set = set()


# Lists #
	#Can be modified - Mutable

courses = ['Physics', 'Math', 'Chemistry', 'Music']
courses_2 = ['Thermodynamics','History']
courses_3 = ['Physical Education','Electronics']
num = [1,6,3,7,2]


print(courses)
	# For length
print(len(courses))

	#Access individual values. 0-indexed
print(courses[0])
		# Use [-x] to access starting from the end of the list
print(courses[-1]) # Prints Chemistry

	#Access range of values; first index inclusive, second isn't
print(courses[0:2])
print(courses[:2])
print(courses[2:]) #Includes last index

	# List Methods #
		#Add item to end of list
courses.append('Art')
print(courses)

		#Add at specific index
courses.insert(0, 'Language')
print(courses)

courses.insert(0, courses_2) #Creates nested list
print(courses)

courses.extend(courses_3) #Adds items from courses_3 to the end as individual items
print courses

		#Remove values
courses.remove('Math')
print(courses)
popped = courses.pop() #Removes last value. Also returns the popped value
print(popped)
print(courses)

		#Reverse List order
courses.reverse()
print(courses)

		#Sorting
courses.sort() #Alphabetical order
num.sort()     #Ascending numerical order
print(courses)
print(num)

num.sort(reverse=True) #Sorts in reverse
print(num)

sorted_num = sorted(courses) #Save sort to another variable
print(sorted_num)

print(min(num)) #Returns smallest value
print(max(num)) #Returns largest value
print(sum(num)) #Returns sum of all values

		#Find index of value
print(courses.index('Music'))

		#Check if value is in list
print('Fish' in courses) #False

for item in courses:  #for loop. item is just a loop variable name
	print(item)       #indented to denote code runs inside of loop

for index, course in enumerate(courses, start=0): #Prints index and value together
	print(index, course)				#Start changes the index number displayed, but not the value at the index


		#List to string
course_str = ', '.join(courses_3) #Creates string in new variable with list values joined by ', '
							#List can only contain strings, no integers or list
print(course_str)

		#String to list
new_list = course_str.split(', ')  #Split string at denoted marker ', ' and return list of the values split up
print(new_list)



# Tuples #
	#Cannot be modified - immutable

	# Mutable
list_1 = ['History','Math','Physics','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art' #Changes list_1 and list_2

	# Immutable
tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'  Does not work


# Sets #
	#Unordered and have no duplicates

mi_courses = {'History','Math','Physics','CompSci','Math'} #Throws away duplicates
crash_courses = {'History','Music','Physics','Sculpting'}

print(mi_courses)

	#Sets are optimized to check for if value is inside
print('Math' in mi_courses) #True

	#Intersection method to see if two sets share values
print(mi_courses.intersection(crash_courses)) #Returns Physics and History

	#Difference method
print(mi_courses.difference(crash_courses)) #Returns CompSci and Math

	#Union method to merge sets
print(mi_courses.union(crash_courses)) #Returns everything together




