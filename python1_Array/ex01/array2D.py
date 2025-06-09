import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	"""
	This function slices a 2D list (family) from start to end index.
	Args:
		family (list): A 2D list where each sublist contains two elements (height and weight).
		start (int): The starting index for slicing.
		end (int): The ending index for slicing.
	Returns:
		list: A new list containing the sliced elements from the family list.
	"""
	assert isinstance(family, list), "Family must be a list."
	assert isinstance(start, int), "Start must be an int."
	assert isinstance(end, int), "End must be an int."
	
	start = start if start >= 0 else start * -1
	end = end if end >= 0 else end * -1
	assert end > start, "End index must be more than start index."

	print(f"My shape is : {np.array(family).shape}")

	new_family = []
	while start < end:
		assert isinstance(family[start], list), "Each family member's data must be a list."
		assert len(family[start]) == 2, "Each family member's data must contain exactly two elements (height and weight)."
		new_family.append(family[start])
		start += 1

	print(f"My new shape is : {np.array(new_family).shape}")
	return new_family

def main():
	try:
		family = [[1.80, 78.4],
		[2.15, 102.7],
		[2.10, 98.5],
		[1.88, 75.2]]
		print(slice_me(family, 0, 2))
		print(slice_me(family, 2, 3))
	except AssertionError as error:
		print("AssertionError:", error)

if __name__ == "__main__":
	main()