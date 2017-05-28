
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is  - check if values have same id / same object in memory


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


language = 'Spanish'

if True:
	print('Conditional was True')

if False:
	print('Conditional was False')

if language == 'French':
	print('French is true')
elif language == 'Spanish':
	print('Language is Spanish')
else:
	print('No French')

# and
# or
# not - changes false to true, and then true to false

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Locked out')

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Locked out')

if not logged_in:  #Evaluates to true
	print('Please log in')
else:
	print('Locked out')


a = [1, 2, 3]
b = [1, 2, 3]

c = a

print(a == b) # Does not check id, only content, so true
print (a is b) # Checks id, so false
print(a is c) #True (id(a) == id(c))

print(id(a))
print(id(b))
print(id(c))





