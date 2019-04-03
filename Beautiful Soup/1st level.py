import urllib.request
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Linkin_Park')
html = response.read()
print (html)
