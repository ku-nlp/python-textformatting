# python-textformatting

## Requirements

- Python 3.6.8

## Installation

```
$ python setup.py install
```

## Example

```python
from textformatting import ssplit

text = "日本語のテキストを文単位に分割します。Pythonで書かれています。"
sentences = ssplit(text)  # ['日本語のテキストを文単位に分割します。', 'Pythonで書かれています。']
```

## License

- MIT

## Authors

- Kyoto University (contact [at] nlp.ist.i.kyoto-u.ac.jp)
  - Hirokazu Kiyomaru
