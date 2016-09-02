# codebottle-python
A Python library to interact with CodeBottle's API.
This is obviously still in development.

##Example:
```python
import codebottle

#Results of a search
search = codebottle.search(keywords="java").results

#Get a snippet
snippet = codebottle.get(id="373dcc67").data

#Browse
browse = codebottle.browse(limit=10).results

#Verify secure
secure = codebottle.verifysecure(secure_token="Some type of token here")
```

##Installing

From git:
```pip install git+https://github.com/codebottle-io/codebottle-python.git```

##TODO:

- Convert dicts to classes
