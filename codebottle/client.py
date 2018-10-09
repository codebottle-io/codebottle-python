import requests
import helpers

headers = {
	'Accept': 'application/vnd.codebottle.v1+json'
}

def _get(url, params=None):
    try:
        req = requests.get(url, headers=headers, params=params)
        return req
    except Exception as e:
        raise e

def search(keywords, language):
    return _get(helpers.apiUrl('/snippets'), params={
        keywords: keywords,
        language: language
    }).json()


def get(id):
    return _get(helpers.apiUrl('/snippets/'.format(id)))


def getLatest():
    return _get(helpers.apiUrl('/snippets/new'))


def getCategories() {
    return _get(helpers.apiUrl('/categories'))


def getCategory(id):
    return _get(helpers.apiUrl('/categories/{0}'.format(id)))


def getLanguages():
    return _get(helpers.apiUrl('/languages'))


def getLanguage(id):
		return _get(helpers.apiUrl('/languages/{0}'.format(id)))
