import pytest

from vntext import remove_accents


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Tiếng Việt", "Tieng Viet"),
        ("Hà Nội", "Ha Noi"),
        ("Phở bò tái", "Pho bo tai"),
        ("Đà Nẵng", "Da Nang"),
        ("đường phố", "duong pho"),
        ("Đ", "D"),
        ("hello world", "hello world"),
        ("", ""),
    ],
)
def test_remove_accents(text, expected):
    assert remove_accents(text) == expected
