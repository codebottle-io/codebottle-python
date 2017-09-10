from codebottle import CodeBottle

cb = CodeBottle()

# Results of a search
search = cb.snippets.get(keywords='java').data

# Get a snippet
snippet = cb.snippets.get('91f98993c8').data

# Browse
browse = cb.snippets.new().data

print(search)
print(snippet)
print(browse)
