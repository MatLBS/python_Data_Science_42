import cv2
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array) -> list:
	"""
	Inverts the color of the image received.
	Args:
		array (list): The image array.
	Returns:
		list: The inverted image array.
	"""
	print(array)
	array_rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
	invert_img = np.subtract(255, array_rgb)
	print(f"Shape invert image is {invert_img.shape}")
	cv2.imwrite('images/invert_img.jpg', invert_img)
	return invert_img


def ft_red(array) -> list:
	"""
	Extracts the red channel from the image and sets the green and blue channels to zero.
	Args:
		array (list): The image array.
	Returns:
		list: The red channel image array.
	"""

	red_rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
	red_rgb[:, :, 0] = 0
	red_rgb[:, :, 1] = 0
	print(f"Shape red image is {red_rgb.shape}")
	cv2.imwrite('images/red_img.jpg', red_rgb)
	return red_rgb


def ft_green(array) -> list:
	"""
	Extracts the green channel from the image and sets the red and blue channels to zero.
	Args:
		array (list): The image array.
	Returns:
		list: The green channel image array.
	"""

	green_rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
	green_rgb[:, :, 0] = 0
	green_rgb[:, :, 2] = 0
	print(f"Shape green image is {green_rgb.shape}")
	cv2.imwrite('images/green_img.jpg', green_rgb)
	return green_rgb


def ft_blue(array) -> list:
	"""
	Extracts the blue channel from the image and sets the red and green channels to zero.
	Args:
		array (list): The image array.
	Returns:
		list: The blue channel image array.
	"""

	blue_img = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
	blue_img[:, :, 1] = 0
	blue_img[:, :, 2] = 0
	print(f"Shape blue image is {blue_img.shape}")
	cv2.imwrite('images/blue_img.jpg', blue_img)
	return blue_img


def ft_grey(array) -> list:
	"""
	Converts the image to grayscale by averaging the BGR channels.
	Args:
		array (list): The image array.
	Returns:
		list: The grayscale image array.
	"""

	(row, col, dim) = array.shape
	grey_img = np.ndarray((row, col, dim), dtype=np.uint8)

	for i in range(row):
		for j in range(col):
			grey_img[i, j] = np.mean(array[i, j])

	print(f"Shape gray image: {grey_img.shape}")
	cv2.imwrite("images/grey_img.jpg", grey_img)
	return grey_img


def main():
	try:
		array = ft_load("images/landscape.jpg")
		ft_invert(array)
		ft_red(array)
		ft_green(array)
		ft_blue(array)
		ft_grey(array)
	except AssertionError as error:
		print(AssertionError.__name__ + ":", error)

if __name__ == "__main__":
	main()