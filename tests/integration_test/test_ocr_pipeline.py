"""
This module contains an integration test for the ocr pipeline.
Uses the real ocr engine.
"""

import pytest  # pyright: ignore[reportMissingImports]
from pymupdf import Document

from file_splitter.os_utils import create_folder
from file_splitter.pdf_instance import PDFInstance
from ocr_engine.tesseract_engine import TesseractEngine
from src.config import TESS_DATA_PATH
from tests.factories import create_test_document


@pytest.mark.parametrize(
    "page_texts, expected_names",
    [
        (
            [
                "Shadow Pte Ltd",
                "Page 5 of 5",
                "Bluewind Pte Ltd",
                "Page 2 of 3",
                "Page 3 of 3",
            ],
            ["Shadow Pte Ltd", "Bluewind Pte Ltd"],
        )
    ],
)
def test_tesseract_pipeline_success(
    tmp_path, page_texts: list[str], expected_names: list[str]
) -> None:
    """
    Tests the tesseract pipeline. Verifies that tesseract is working as expected.
    """

    doc: Document = create_test_document(text=page_texts)
    tesser_engine: TesseractEngine = TesseractEngine(tess_data_path=TESS_DATA_PATH)
    test_instance: PDFInstance = PDFInstance(tesser_engine, tmp_path, create_folder)
    test_instance.split_statements(doc)
    split_files = list(tmp_path.glob("**/*.pdf"))
    split_names = [file.name for file in split_files]
    for name in expected_names:
        assert any(name in filename for filename in split_names)
        # returns True as long as at least one name is in split_names
