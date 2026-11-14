# vntext

[![CI](https://github.com/thienta-oss-lab/vntext/actions/workflows/ci.yml/badge.svg)](https://github.com/thienta-oss-lab/vntext/actions/workflows/ci.yml)

Small, dependency-free utilities for Vietnamese text.

- `remove_accents` — strip Vietnamese diacritics
- `slugify` — build URL-friendly slugs
- `to_words` — read integers as Vietnamese words

## Installation

```bash
pip install git+https://github.com/thienta-oss-lab/vntext.git
```

## Quick start

```python
from vntext import remove_accents, slugfy, to_words

remove_accents("Tiếng Việt")  # 'Tieng Viet'
slugify("Xin chào Việt Nam!")  # 'xin-chao-viet-nam'
to_words(1234)  # 'một nghìn hai trăm ba mươi bốn'
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before
opening an issue or a pull request. Issues labelled
[`good first issue`](https://github.com/thienta-oss-lab/vntext/labels/good%20first%20issue)
are a great place to start.

## License

[MIT](LICENSE)
