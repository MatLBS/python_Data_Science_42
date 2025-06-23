import matplotlib.pyplot as plt
import os


def ft_load(path: str) -> list:
    """
    This function loads an image from the specified path
    and returns a list of its pixels
    content in RGB format.
    Args:
        path (str): The file path to the image.
    Returns:
        list: A list of the image's pixels in RGB format.
    """

    assert os.path.exists(path), "The specified path does not exist."
    img = plt.imread(path)
    assert img is not None, (
        "Image could not be loaded. Please check the file path."
    )
    print(f"The shape of image is {img.shape}")

    subset = img[0:3, 0:3]
    return subset


def main():
    try:
        print(ft_load("landscape.jpg"))
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
