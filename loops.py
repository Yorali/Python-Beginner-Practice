 
nums = [1, 2, 3, 4, 5]

# for loops #

for num in nums:
	if num == 3:
		print('Found')
		break 		#Break statement breaks out of for loop
	print(num)


for num in nums:
	if num == 3:
		print('Found')
		continue    #Continue to skip a value
	print(num)


# loops within loops #

for num in nums:
	for letter in 'abc':
		print(num, letter)

# Range #

for i in range(10): #Goes up to but not including 10
	print(i)

	# Can also take 2 arguments
for i in range(1, 11):
	print(i)


# While-loop #
	# Keeps going until certain conditions are met
x = 0

while x < 10:
	print(x) # Break statements can also be used
	x += 1   # control + c can be used to cancel operation







