"""
This module tests the pdf_instance file to ensure its state management is behaving correctly.
"""

from unittest.mock import MagicMock, create_autospec, patch
import pytest
from file_splitter.pdf_instance import PDFInstance
from ocr_engine.base import OCREngine


def test_pdf_instance_init():
    """
    Sanity check: correct default values
    """

    mock_engine = MagicMock()
    mock_str = "pathxxx"
    mock_create_folder = MagicMock()
    mock_output = MagicMock()

    mock_create_folder.return_value = mock_output

    test_instance = PDFInstance(mock_engine, mock_str, mock_create_folder)

    assert test_instance._ocr_engine == mock_engine
    assert test_instance._output_folder == mock_output
    assert test_instance._page_buffer == []
    assert test_instance._current_name is None


@pytest.mark.parametrize(
    "page_texts, flush_count",
    [(["ACME Pte Ltd", "Shadow Ronin Mifune Pte Ltd", "asdohjasfuodfh"], 2)],
)
def test_pdf_instance_split_statements(page_texts, flush_count):
    """
    Tests the behaviour of split_statements through external input and output.
    This test verifies that split_statements calls ._flush the correct number of times
    ('flush_count') corresponding to the input ('page_texts').
    """

    mock_ocr = create_autospec(OCREngine)  # pyright: ignore[reportAny]
    mock_parent_dir = MagicMock()
    mock_folder_path = MagicMock()
    mock_doc = MagicMock()
    # we should set mock_doc.__len__ because split_statements iterates over it.
    # however, it is not necessary because we directly patch process_doc, which is dependent on
    # mock_doc. We do it anyways.
    mock_doc.__len__.return_value = len(page_texts)
    mock_instance = PDFInstance(
        ocr_engine=mock_ocr,
        runtime_parent_dir=mock_parent_dir,
        create_folder_path=mock_folder_path,
    )

    with patch.object(PDFInstance, "_flush") as mock_flush:
        mock_ocr.process_doc.return_value = list(enumerate(page_texts))

        mock_instance.split_statements(mock_doc, True)

        mock_ocr.process_doc.assert_called_once_with(mock_doc)
        assert mock_flush.call_count == flush_count
