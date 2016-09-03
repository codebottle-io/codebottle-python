import requests

api_version = "v1"
api_url = "https://codebottle.io/api/{0}".format(api_version)

api_search_url = "{0}/search.php".format(api_url)
api_get_snippet_url = "{0}/get.php".format(api_url)
api_browse_url = "{0}/browse.php".format(api_url)
api_verifysecure_url = "{0}/verifysecure.php".format(api_url)


class CodebottleError(Exception):
	"""Exception to represent a error sent from the API"""
	pass

class Result(object):
	"""A class with attributes of a codebottle API result"""
	def __init__(self, r):
		self.json = r.json()
		if self.json["error"]:
			raise CodebottleError(self.json["error"])

		for k, v in self.json.items():
			setattr(self, k, v)

#Functions
def search(**kwargs):
	result = requests.get(api_search_url, params=kwargs)
	return Result(result)

def get(**kwargs):
	result = requests.get(api_get_snippet_url, params=kwargs)
	return Result(result)

def browse(**kwargs):
	result = requests.get(api_browse_url, params=kwargs)
	return Result(result)

def verifysecure(**kwargs):
	result = requests.get(api_verifysecure_url, params=kwargs)
	return Result(result)
