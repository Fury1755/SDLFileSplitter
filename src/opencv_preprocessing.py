"""
This module handles preprocessing of pdf pages for OCR.
"""

import cv2
import numpy as np
from deskew import determine_skew


def deskew_image(img_grey: np.ndarray) -> np.ndarray:
    """
    Uses the deskew library to determine skew angles in a greyscale image.
    Returns a new deskewed numpy array.

    Args:
        img_grey(np.ndarray): greyscale image as numpy array
    Returns:
        A new deskewed numpy array
    """

    angle = determine_skew(img_grey)

    if angle is None:
        return img_grey

    h, w = img_grey.shape[:2]
    centre = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(centre, angle, 1.0)

    rotated = cv2.warpAffine(
        img_grey,
        rotation_matrix,
        (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=255,
    )

    return rotated


def preprocess(img: np.ndarray) -> np.ndarray:
    """
    Args:
        img(np.ndarray): OpenCV image as numpy array
    Returns:
        Preprocessed image (BGR) as numpy array
    """

    # pylint: disable=E1101

    # we skip greyscale because pymupdf already loads the pixmap as
    #  grayscale

    img = deskew_image(img)

    denoised = cv2.bilateralFilter(img, 9, 75, 75)

    # THRESH_BINARY turns every pixel below the threshold white, and every
    #  pixel above the threshold black.
    # THRESH_OTSU figures out what the threshold value should be by seeing
    #  where the variance between two groups is minimized/maximized.
    _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return binary
