def square(x: int | float) -> int | float:
	assert isinstance(x, (int, float)), "The value must be integer or float"
	assert x != 0, "You can not divide by 0"
	return x**2

def pow(x: int | float) -> int | float:
	return x**x

# def outer(x: int | float, function) -> object:
# 	def inner() -> float:
# 		count = 0
# 		if count == 0:
# 			count = function(x)
# 		else:
# 			count = function(count)
# 		return count
# 	return inner

def outer(x: int | float, function) -> object:
	current = x

	def inner() -> float:
		nonlocal current
		current = function(current)
		return current

	return inner

def main():
	try:
		my_counter = outer(3, square)
		print(my_counter())
		print(my_counter())
		print(my_counter())
		print("---")
		another_counter = outer(1.5, pow)
		print(another_counter())
		print(another_counter())
		print(another_counter())
	except AssertionError as error:
		print("AssertionError:", error)


if __name__ == "__main__":
	main()
