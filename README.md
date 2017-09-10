# codebottle-python  [![Build Status](https://travis-ci.org/codebottle-io/codebottle-python.svg?branch=master)](https://travis-ci.org/codebottle-io/codebottle-python)
A Python library to interact with CodeBottle's API.
This is obviously still in development.

## Example:
```python
from codebottle import CodeBottle

cb = CodeBottle()

# Results of a search
search = cb.snippets(keywords='java').data

# Get a snippet
snippet = cb.snippets('91f98993c8').data

# Get newest snippets
browse = cb.snippets('new').results
```

## Installing

From git:
```pip install git+https://github.com/codebottle-io/codebottle-python.git```

## TODO:

- Convert dicts to classes
