"""
Orchestrator module. There should be no external dependencies here!
"""

import logging

import pymupdf

from tesseract.tesseract_orchestrator import extract_text_from_pdf
from config import PDF_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelno)s - %(funcName)s - %(message)s",
)

pdf = pymupdf.open(PDF_PATH)

# text_stream is a generator that returns
#  the corresponding iterable when called.
text_stream = extract_text_from_pdf(pdf)
for page_number, page_text in text_stream:
    logging.info("Page %s scanned", page_number)
