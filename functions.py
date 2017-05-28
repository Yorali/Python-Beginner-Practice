
def hello_funcn():
	pass     # Use to skip a blank function to avoid errors

def hello_func():
	return 'Hello Function' # Sets functions as equal to this value

print(hello_func()) #Prints a string, so str methods can be used on hello_func

print(hello_func().upper())


def hello(greeting, name = 'You'): # Set default value to name
	return '{}, {}.'.format(greeting, name)

print(hello('Howdy')) # Name prints default value, since not defined here

print(hello('Hello','Time'))



def student_info(*args, **kwargs):
	print(args) #Positional arguments
	print(kwargs) #Key-word values

student_info('Math','Art', name='Akira', age=25)  #Returns tuple for args, and dict for kwargs

def student2_info(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Physics', 'Music']
info = {'name': 'Saki', 'age': 27}

student2_info(*courses, **info) #Must include *'s to unpack correctly


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]








