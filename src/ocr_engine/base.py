"""
An abstract base class that contains an interface, allowing us to swap out different OCR models easily
"""

from abc import ABC, abstractmethod
from typing import Tuple, Iterator

from pymupdf import Page, Document
import numpy as np


class OCREngine(ABC):
    """
    Each engine handles its own preprocessing, document processing and page extraction.
    """

    @abstractmethod
    def _preprocess(self, img: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def process_doc(self, doc: Document) -> Iterator[Tuple[int, str]]:
        pass

    @abstractmethod
    def process_page(self, page: Page) -> str:
        pass
