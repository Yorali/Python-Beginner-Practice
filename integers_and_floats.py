
num = 7
num2 = 3.14

# 1.) Show data type of argument
print(type(num))
print(type(num2))

# Arithmetic Operators:
	# Addition:        5 + 4
	# Subtraction:     5 - 4
	# Multiplication:  5 * 4
	# Division:        5 / 4
	# Floor division:  5 // 4 Prevents decimal drop in older Python
	# Exponent:        5 ** 4
	# Modulus:         5 % 4  Gives remainder after division. Can be used to check if even or odd

print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)

# Order of operations is normal in Python

# 2.) Shorthand
num += 1
num2 *= 100

print(num)
print(num2)

# 3.) Absolute values
print(abs(-4))

# 4.) Round to nearest integer. Second argument dictates number of decimal places to round to
print(round(2.52, 1))
print(round(2.40))

# Comparisons:
	# * '=' is used for assignment, not comparison *
	# Equal:			==
	# Not Equal:		!=
	# Greater Than:		>
	# Less Than:		<
	# Greater or Equal:	>=
	# Less or Equal:	<=

num_1 = 6
num_2 = 8

print(num_1 == num_2) # Returns false
print(num_1 != num_2) # Returns true

# 5.) Must use casting to avoid the following

num_12 = '100'
num_13 = '200'

print(num_12 + num_13) # Returns 100200, because the variables have numbers as strings, not integers

	# Cast by using int()
num_12 = int(num_12)
num_13 = int(num_13)

print(num_12 + num_13)





