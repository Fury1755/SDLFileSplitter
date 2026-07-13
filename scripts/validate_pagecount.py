"""
One-off renaming script
"""

import os

import pymupdf

directory = r"C:\Users\Intern\Downloads\SDLsplit_20260707_131813"

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    pdf = pymupdf.open(filepath)
    page_no = len(pdf)
    if page_no != 4 and page_no != 6:
        print(f"File {filename} has invalid page count")
