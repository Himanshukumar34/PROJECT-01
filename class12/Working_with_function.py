"""Simple notes on Python functions for Class 12 students.

What is a function?
- A function is a named block of code. Use `def` to make one.

How to write a function
- `def name(parameters):` then write the code indented below.
- Use `return` to send back a result.

Easy examples

	return "Hello, " + name

def add(a, b=0):
	"""Return sum of a and b. b is optional."""
	return a + b

def sum_all(*nums):
	"""Return total of all numbers given."""
	total = 0
	for n in nums:
		total += n
	return total

if __name__ == "__main__":
	print(greet("World"))
	print(add(5))
	print(add(2, 3))
	print(sum_all(1, 2, 3, 4))
"""
