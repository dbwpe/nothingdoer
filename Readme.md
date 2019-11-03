# NothingDoer

Do you need to do nothing?  NothingDoer can do that.
It also logs what it (doesn't) do.

## Installation

Not on pypi at the moment, so:

```
git clone https://github.com/gulducat/nothingdoer.git
cd nothingdoer
python setup.py install
```

## Usage

```
>>> import logging
>>> from nothingdoer import NothingDoer
>>>
>>> logging.basicConfig(level=logging.DEBUG)
>>>
>>> nd = NothingDoer()
>>> nd.ok == nd
DEBUG:nothingdoer:"ok" is a NothingDoer
True
>>> nd['ok'] == nd
DEBUG:nothingdoer:"ok" is a NothingDoer
True
>>> nd.ok() == nd
DEBUG:nothingdoer:"ok" is a NothingDoer
DEBUG:nothingdoer:call args: (); kwargs: {}
True
```

with a callback:

```
>>> def callback(nd, *a, **kw):
...     return 'did something with {} and {}'.format(a, kw)
...
>>> nd = NothingDoer(callback=callback)
>>> print(nd('ok', yea='sure'))
DEBUG:nothingdoer:call args: ('ok',); kwargs: {'yea': 'sure'}
did something with ('ok',) and {'yea': 'sure'}
```