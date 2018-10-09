apiBase = 'https://api.codebottle.io/';

def apiUrl(url):
	return apiBase + (url[1:] if url.find('/') == 0 else url)
