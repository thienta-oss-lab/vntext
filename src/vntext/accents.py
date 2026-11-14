import unicodedata

# Vietnamese đ/Đ carry no combining mark, so NFD decomposition leaves them intact.
_STROKE_D = str.maketrans({"đ": "d", "Đ": "D"})


def remove_accents(text: str) -> str:
    """Remove Vietnamese diacritics from ``text``.

    >>> remove_accents("Tiếng Việt")
    'Tieng Viet'
    >>> remove_accents("Đà Nẵng")
    'Da Nang'
    """
    decomposed = unicodedata.normalize("NFD", text)
    stripped = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", stripped.translate(_STROKE_D))
