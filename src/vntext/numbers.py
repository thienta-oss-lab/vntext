DIGITS = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
SCALES = ["", "nghìn", "triệu", "tỷ"]
MAX_VALUE = 10**12 - 1


def _read_group(number: int, full: bool) -> list[str]:
    """Read a group of three digits (0-999).

    ``full`` is True when the group is not the leading group, so missing
    hundreds must still be read ("không trăm").
    """
    hundreds, rest = divmod(number, 100)
    tens, units = divmod(rest, 10)
    words: list[str] = []

    if hundreds or full:
        words += [DIGITS[hundreds], "trăm"]

    if tens == 0:
        if units and words:
            words.append("linh")
    elif tens == 1:
        words.append("mười")
    else:
        words += [DIGITS[tens], "mươi"]

    if units:
        words.append(DIGITS[units])

    return words


def to_words(number: int) -> str:
    """Read an integer as Vietnamese words.

    >>> to_words(1234)
    'một nghìn hai trăm ba mươi bốn'
    """
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an int")
    if abs(number) > MAX_VALUE:
        raise ValueError(f"number must be between -{MAX_VALUE} and {MAX_VALUE}")
    if number == 0:
        return DIGITS[0]
    if number < 0:
        return "âm " + to_words(-number)

    groups: list[int] = []
    while number:
        number, group = divmod(number, 1000)
        groups.append(group)

    words: list[str] = []
    for index in range(len(groups) - 1, -1, -1):
        group = groups[index]
        if group == 0:
            continue
        is_leading = index == len(groups) - 1
        words += _read_group(group, full=not is_leading)
        if SCALES[index]:
            words.append(SCALES[index])

    return " ".join(words)
