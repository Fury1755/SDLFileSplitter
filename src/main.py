"""
Orchestrator module. There should be no external dependencies here!
"""

import io
import datetime

from PIL import Image
import tesserocr
import pymupdf

from config import PDF_PATH, TESS_DATA_PATH

if TESS_DATA_PATH is None:
    raise RuntimeError("TESS_DATA_PATH not set!")
with tesserocr.PyTessBaseAPI(path=TESS_DATA_PATH) as api:  # pylint: disable=E1101
    doc = pymupdf.open(PDF_PATH)

    # get a pixmap (image)
    pix = doc[0].get_pixmap()

    img = Image.open(io.BytesIO(pix.tobytes("png")))

    time = datetime.datetime.now()
    # SetImage loads the image into the engine
    api.SetImage(img)

    text = api.GetUTF8Text()
    new_time = datetime.datetime.now()
    print(text)
    delta_time = new_time - time
    api.End()
    print(delta_time)
