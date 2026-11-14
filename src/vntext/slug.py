import re

from vntext.accents import remove_accents


def slugify(text: str) -> str:
    """Turn ``text`` into a URL-friendly slug.

    >>> slugify("Xin chào Việt Nam!")
    'xin-chao-viet-nam'
    """
    text = remove_accents(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
