"""Small utilities for Vietnamese text."""

from vntext.accents import remove_accents
from vntext.numbers import to_words
from vntext.slug import slugify

__all__ = ["remove_accents", "slugify", "to_words"]
__version__ = "0.1.0"
