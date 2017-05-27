# Prints welcome message
# Hit cmb + b to run Python script in Sublime


#Setting variable. ';' not needed at end, Python is a white-space language
#Convention: my_message; underscores are used
# \' can be used to use ' inside of ''

message = "Koga's World"

# 1.) Print argument
print(message)

# 2.) Print string
print("Koga's World")

# 3.) Print length of argument
print(len(message))

# 4.) Print index of argument. This is 0-indexed
print(message[0])
	# a.) Print from a range. First index inclusive, second is not, so message[3] is last character printed
print(message[0:4])
	# b.) Can also slice...
print(message[:4])
print(message[4:])

# 5.) A method and function are almost the same, but a method belongs to an object

# ~Various methods~

# 6.) Change case of string/argument string
print(message.lower())
print(message.upper())

# 7.) Count number of instances of a character in argument -CASE SENSITIVE-
print(message.count('K'))
print(message.count('o'))
print(message.count('k'))

# 8.) Find index of argument
print(message.find('Koga')) #Koga starts at [0], so prints 0
print(message.find('World')) #World starts at [7]
print(message.find('Deviled Eggs')) #Doesn't exist, so [-1]


# 9.) Replace first argument with second
message.replace('World','Bass')
	# However, does not change original variable. Just creates a string
print(message)
	# Create a new variable...
new_message = message.replace('World','Bass')
print(new_message)
	# OR set original variable to new self
message = message.replace('World','Bass')
print(message)

# 10.) Concatenate strings
greeting = 'Good Evening'
name = 'Emi'

say_hi = greeting + ', ' + name + '. Welcome!'
print(say_hi)
	# Can use placeholders {} as well
say_hello = '{}, {}. Welcome!'.format(greeting, name)
	# format arguments correspond to the placeholders
print(say_hello)
	# f-strings can be used to place variables right in placeholder, and even run functions on the variables inside
	# Python 3.6 and above
#say_hey = f'{greeting}, {name}. Welcome!'
#print(say_hey)

# 11.) Show all attributes and methods associated with a variable
print(dir(name))
	# Give more information about
print(help(str))
	# Give info about a method
print(help(str.lower))




