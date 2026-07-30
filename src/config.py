"""
Fetches runtime constants from .env
"""

import os

from dotenv import load_dotenv

load_dotenv()

PDF_PATH = os.environ.get("PDF_PATH")
TESS_DATA_PATH = os.environ.get("TESS_DATA_PATH")
RUNTIME_PARENT_DIR = os.environ.get("RUNTIME_PARENT_DIR")
DEBUG_PDF_PATH = os.environ.get("DEBUG_PDF_PATH")
