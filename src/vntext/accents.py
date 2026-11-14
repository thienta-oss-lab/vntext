import unicodedata


def remove_accents(text: str) -> str:
    """Remove Vietnamese diacritics from ``text``.

    >>> remove_accents("Tiếng Việt")
    'Tieng Viet'
    """
    decomposed = unicodedata.normalize("NFD", text)
    stripped = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", stripped)
