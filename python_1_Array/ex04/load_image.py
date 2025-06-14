import cv2
import os


def ft_load(path: str) -> list:
    """
    This function loads an image from the specified
    path and returns a list of its pixels
    content in RGB format.
    Args:
        path (str): The file path to the image.
    Returns:
        list: A list of the image's pixels in RGB format.
    """

    assert os.path.exists(path), "The specified path does not exist."
    img = cv2.imread(path)
    assert img is not None, (
        "Image could not be loaded. Please check the file path."
    )
    print(f"The shape of image is {img.shape}")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    assert img_rgb is not None, "Image could not be converted to RGB format."

    subset = img_rgb[0:3, 0:3]
    return subset
