"""
Orchestrator module. There should be no external dependencies here!
"""

import logging

import pymupdf

from src.ocr_engine.tesseract_engine import TesseractEngine
from src.file_splitter.pdf_instance import PDFInstance
from src.file_splitter.os_utils import (
    create_folder,
)  # temporary monkey patch until new rules are introduced
from src.config import PDF_PATH, TESS_DATA_PATH, RUNTIME_PARENT_DIR

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelno)s - %(funcName)s - %(message)s",
)

pdf = pymupdf.open(PDF_PATH)

tesser_eng = TesseractEngine(TESS_DATA_PATH)
pdf_splitter = PDFInstance(
    tesser_eng, RUNTIME_PARENT_DIR, create_folder
)  # note: monkey patch
pdf_splitter.split_statements(pdf)
