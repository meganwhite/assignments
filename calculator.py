
# Multiply
def multiply(a,b):
	return a * b

# Add
def add(a,b):
	return a + b

# Subtract
def subtract(a,b):
	return a - b

# Divide
def divide(a,b):
	return a/b

# Square
def square(a):
	return a * a

# Cube
def cube(a):
	return a * a * a

# Square n times
def square_n_times(number,n):
	i = 1
	while i <= n:
		number = square(number)
		i += 1
	return number

print "I'm going to use the calculator functions to divide 30 by 5"
x = divide(30,5)
print x

print "I'm going to use the caluclator to square 2 3 times."
y = square_n_times(2,3)
print y