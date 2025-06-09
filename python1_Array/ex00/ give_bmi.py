def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""
	This function calculates the Body Mass Index (BMI) for each pair of height and weight.
	Args:
		height (list[int | float]): A list of heights in meters.
		weight (list[int | float]): A list of weights in kilograms.
	Returns:
		list[int | float]: A list of BMI values calculated as weight divided by the square of height.
	"""
	




def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""
	This function checks if each BMI value is below a specified limit.
	Args:
		bmi (list[int | float]): A list of BMI values.
		limit (int): The limit to compare against.
	Returns:
		list[bool]: A list of boolean values indicating whether each BMI is below the limit.
	"""
	print("cc")

def main():
	height = [2.71, 1.15]
	weight = [165.3, 38.4]
	bmi = give_bmi(height, weight)
	print(bmi, type(bmi))
	print(apply_limit(bmi, 26))

if __name__ == "__main__":
	main()