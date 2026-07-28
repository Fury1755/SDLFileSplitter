"""
This module contains an integration test for the ocr pipeline.
Uses the real ocr engine.
"""

from pymupdf import Document

from file_splitter.os_utils import create_folder
from file_splitter.pdf_instance import PDFInstance
from ocr_engine.tesseract_engine import TesseractEngine
from src.config import TESS_DATA_PATH
from tests.factories import create_test_document


def test_tesseract_pipeline(tmp_path) -> None:
    """
    Tests the tesseract pipeline. Verifies that tesseract is working as expected.
    """

    page_texts: list[str] = ["Shadow Pte Ltd", "Page 5 of 5"]
    doc: Document = create_test_document(text=page_texts)
    tesser_engine: TesseractEngine = TesseractEngine(tess_data_path=TESS_DATA_PATH)
    test_instance: PDFInstance = PDFInstance(tesser_engine, tmp_path, create_folder)
    test_instance.split_statements(doc)
    split_files = list(tmp_path.glob("**/*.pdf"))
    file_names = [file.name for file in split_files]
    assert "Shadow Pte Ltd" in file_names[0]
