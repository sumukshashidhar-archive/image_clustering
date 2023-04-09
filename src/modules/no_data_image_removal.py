import cv2


def check_nodata_image(path, threshold=5):
    """
    Given an image path, load the image, convert it to grayscale,
    and check if there is very little difference among the pixels
    in the image. If there is, then output true, else, output false.

    Parameters:
        - path (str): Path of the image file.
        - threshold (int): The maximum difference between the
                           pixel values to be considered as similar.

    Returns:
        - bool: True if the difference among the pixel values is
                less than the threshold, False otherwise.
    """

    # Load the image using cv2.imread()
    image = cv2.imread(path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Downscale the image to reduce computation time and increase performance
    scale_factor = 0.3
    downscaled_image = cv2.resize(gray_image, None, fx=scale_factor, fy=scale_factor)

    # Calculate the standard deviation of the pixel values in the image
    std_dev = downscaled_image.std()

    # Check if the standard deviation is less than the threshold
    return std_dev < threshold
