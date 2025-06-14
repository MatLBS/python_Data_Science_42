import numpy as np
import matplotlib.pyplot as plt


def rotate_axis(img: list) -> list:
    """
    This function rotates the given image by 90 degrees anticlockwise.
    Args:
        img (list): A 2D list representing the image pixels.
    Returns:
        list: A new 2D list representing the rotated image pixels.
    """

    new_img = np.ndarray(shape=(400, 400))

    for i in range(len(img)):
        for j in range(len(img)):
            new_img[len(img) - 1 - j][i] = img[i][j]
    return new_img


def ft_rotate(path: str) -> list:
    """
    This function loads an image from the specified
    path, zooms in on a specific region,
    converts it to grayscale, rotates it by 90 degrees
    anticlockwise, and displays the image.
    Args:
        path (str): The file path to the image.
    Returns:
        list: The rotated grayscale image.
    """

    img = plt.imread(path)
    zoomed_img = img[100:500, 450:850]
    gray_image = zoomed_img[:, :, 1]    # 0 = Red; 1 = Green; 2 = Blue
    h, w = gray_image.shape
    print(f"The shape of image is: {h, w, 1} or {gray_image.shape}")

    plt.imshow(gray_image, cmap="gray")
    plt.title("Zoomed + Gray Image")
    plt.axis('on')
    plt.show()

    new_img = rotate_axis(gray_image)

    gray_image = np.expand_dims(gray_image, axis=2)
    subset = gray_image[0:3, 0:3]
    print(subset)

    print(f"New shape after Transpose: {new_img.shape}")

    plt.imshow(new_img, cmap="gray")
    plt.title("Zoomed + Gray + Rotated Image")
    plt.axis('on')
    plt.show()

    return new_img


def main():
    try:
        print(ft_rotate("animal.jpeg"))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
