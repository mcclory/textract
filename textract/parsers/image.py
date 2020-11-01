"""
Process an image file using tesseract.
"""
import os

from .utils import ShellParser


def get_tesseract_path():
    return os.getenv("TEXTRACT_TESSERACT_PATH", "tesseract")


class Parser(ShellParser):
    """Extract text from various image file formats using tesseract-ocr"""

    def extract(self, filename, **kwargs):

        # if language given as argument, specify language for tesseract to use
        if "language" in kwargs:
            args = [get_tesseract_path(), filename, "stdout", "-l", kwargs["language"]]
        else:
            args = [get_tesseract_path(), filename, "stdout"]

        stdout, _ = self.run(args)
        return stdout
