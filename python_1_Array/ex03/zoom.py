import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(path: str) -> list:
    """
    This function loads an image from the
    specified path, zooms into a specific region,
    and returns the zoomed image in gray.
    Args:
        path (str): The file path to the image.
    Returns:
        np.ndarray: The zoomed image in gray format.
    """

    img = ft_load(path)

    print(img)
    plt.title("Normal Image")
    plt.axis('off')
    plt.imshow(img)
    plt.show()

    zoomed_img = img[100:500, 450:850]
    plt.imshow(zoomed_img)
    plt.title("Zoomed Image")
    plt.axis('off')
    plt.show()

    gray_image = zoomed_img[:, :, 1]  # 0 = Red; 1 = Green; 2 = Blue

    plt.imshow(gray_image, cmap="gray")
    plt.title("Zoomed + Gray Image")
    plt.axis('on')
    plt.show()

    h, w = gray_image.shape
    print(f"New shape after slicing: {h, w, 1} or {gray_image.shape}")
    gray_image = np.expand_dims(gray_image, axis=2)
    return gray_image


def main():
    try:
        print(ft_zoom("animal.jpeg"))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
