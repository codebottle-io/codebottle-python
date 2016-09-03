import codebottle

#Results of a search
search = codebottle.search(keywords="java").results

#Get a snippet
snippet = codebottle.get(id="373dcc67").data

#Browse
browse = codebottle.browse(limit=10).results

print(search)
print(snippet)
print(browse)
