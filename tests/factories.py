"""
Utility module for creating test objects.
"""

from unittest.mock import MagicMock

from pymupdf import Document, Page

from src.file_splitter.pdf_instance import PDFInstance


def create_page_list(text: list[str], doc: Document) -> list[Page]:
    """
    Creates a list of pymupdf.Page objects with text inside it. Used for testing internal functions
    of PDFInstance.

    Args:
        text(list[str]): A list of strings. The number of pages correspond to the number of
                        strings in the list.
        doc(pymupdf.Document): A document passed externally as a dependency. Used so that
                                the individual pages don't lose the value of their page.number
                                attributes.

    Returns:
        A list containing pymupdf.Page objects. The index of each page contains text
        corresponding to the index of the strings in the list.
    """

    page_list: list[Page] = []
    for page_text in text:
        doc.new_page()

    for i, page_text in enumerate(text):
        doc[i].insert_text((50, 50), page_text)
        page_list.append(doc[i])
    return page_list


def create_test_document(text: list[str]) -> Document:
    """
    Returns a pymupdf.Document with one page per string.
    """

    # virtually same as above but we return doc instead of page_list
    doc = Document()
    for page_text in text:
        doc.new_page()

    for i, page_text in enumerate(text):
        doc[i].insert_text((50, 50), page_text)
    return doc


class TestablePDFInstance(PDFInstance):  # this is inheritance, not composition
    """
    Wrapper around PDFInstance. Has private methods that manually set internal state
    of PDFInstance for testing.
    """

    # stops pytest from looking for tests in this class, which will raise a warning
    __test__ = False

    def __init__(self, **kwargs):
        """
        Initializes with default values for testing purposes
        """
        self._ocr_engine = MagicMock()
        self._runtime_parent_dir = "blah"
        self._page_buffer = []
        self._current_name = None
        self._output_folder = "blah blah"

    def set_flush_state(self, page_list: list[Page], name: str):
        """
        Sets its state to be flushed
        """
        self._page_buffer = page_list
        self._current_name = name

    def test_flush(self):
        """
        Expose the private _.flush method so testing doesn't violate encapsulation.
        """
        self._flush()
