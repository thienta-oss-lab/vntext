import pytest

from vntext import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Xin chào Việt Nam!", "xin-chao-viet-nam"),
        ("  Hello   World  ", "hello-world"),
        ("Phở 24h", "pho-24h"),
        ("Đà Nẵng", "da-nang"),
        ("đường phố", "duong-pho"),
        ("---", ""),
        ("", ""),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected
