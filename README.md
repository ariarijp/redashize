# redashize

Convert list of dict to Redash-styled dict.

## Installation

```bash
$ pip install git+https://github.com/ariarijp/redashize
```

## Usage

```python
>>> import pprint
>>> from redashize import redashize
>>> rows = [
...     {'a': 1, 'b': 0.2, 'c': 'foo'},
...     {'a': 2, 'b': 0.4, 'c': 'bar'},
...     {'a': 3, 'b': 0.6, 'c': 'baz'},
... ]
>>> result = redashize(rows)
>>> pprint.pprint(result)
{'columns': [{'friendly_name': 'a', 'name': 'a'},
             {'friendly_name': 'b', 'name': 'b'},
             {'friendly_name': 'c', 'name': 'c'}],
 'rows': [{'a': 1, 'b': 0.2, 'c': 'foo'},
          {'a': 2, 'b': 0.4, 'c': 'bar'},
          {'a': 3, 'b': 0.6, 'c': 'baz'}]}
```

### If you want to use it with Python 3.5 or other lower version of Python

Python 3.5 or lower version's dict doesn't have order.

You should sort `'columns'` values by yourself or you can use list of OrderedDict instead of list of dict.

## License

MIT

## Author

[ariarijp](https://github.com/ariarijp)