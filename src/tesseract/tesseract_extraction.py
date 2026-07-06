"""
This module is the OCR engine of the script!
Dependencies:
    tesserocr
        extracts text from PIL's Image
    PIL
        converts numpy array to Image
    numpy
        for type hints
"""

from tesserocr import PyTessBaseAPI  # pylint: disable=E0611
from PIL import Image
import numpy as np


def extract_text(img_np: np.ndarray, api: PyTessBaseAPI) -> str:
    """
    Extracts text from a single page using a pre-existing tesseract API instance.

    Args:
        img(np.ndarray): The image's numpy array

        api(PyTessBaseAPI): A pre-existing PyTessBaseAPI instance

    Returns:
        A string containing the contents of the page.
    """

    # convert to PIL Image
    pil_img = Image.fromarray(img_np)

    # pass the PIL Image into the engine
    api.SetImage(pil_img)

    # run the engine and extract the text
    text = api.GetUTF8Text()

    return text
