import pytest

from vntext import to_words


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, "không"),
        (7, "bảy"),
        (10, "mười"),
        (12, "mười hai"),
        (20, "hai mươi"),
        (99, "chín mươi chín"),
        (100, "một trăm"),
        (101, "một trăm linh một"),
        (110, "một trăm mười"),
        (1000, "một nghìn"),
        (1005, "một nghìn không trăm linh năm"),
        (1234, "một nghìn hai trăm ba mươi bốn"),
        (1_000_000, "một triệu"),
        (2_000_000_000, "hai tỷ"),
        (-3, "âm ba"),
    ],
)
def test_to_words(number, expected):
    assert to_words(number) == expected


@pytest.mark.parametrize("value", [1.5, "12", None, True])
def test_to_words_rejects_non_int(value):
    with pytest.raises(TypeError):
        to_words(value)


@pytest.mark.parametrize("value", [10**12, -(10**12)])
def test_to_words_rejects_out_of_range(value):
    with pytest.raises(ValueError):
        to_words(value)
