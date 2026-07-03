"""
Orchestrator that initializes an API instance and streams the result
"""

# pylint: disable=E0611
from typing import Tuple, Iterator

import pymupdf
from tesserocr import PyTessBaseAPI

from pdf_to_nparray import page_to_numpy
from opencv_preprocessing import preprocess
from tesseract.tesseract_extraction import extract_text
from config import TESS_DATA_PATH


def extract_text_from_pdf(pdf: pymupdf.Document) -> Iterator[Tuple[int, str]]:
    """
    Lazily streams tuples containing the page number and the text contents of a pdf.

    Args:
        pdf(pymupdf.Document): The pdf's structure (not the entire pdf!) loaded into memory
    Returns:
        A generator object that returns Tuples sequentially when called.
        The tuple contains the page number, and the page contents respectively.
        Example: [0, "The first page"]
    """

    # initialize the api
    if TESS_DATA_PATH is None:
        raise RuntimeError(
            "tesseract.tesseract_orchestrator.py received None in TESS_DATA_PATH"
        )
    with PyTessBaseAPI(path=TESS_DATA_PATH) as api:
        for i in range(len(pdf)):  # pylint: disable=C0200
            page = pdf[i]
            # page_to_numpy loads the page into memory individually
            page_nparray = page_to_numpy(page)
            preprocessed = preprocess(page_nparray)
            yield (i, extract_text(preprocessed, api))
    api.End()
