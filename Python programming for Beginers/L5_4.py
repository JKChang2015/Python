import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen('http://helloworldbook.com/data/message.txt')
message = file.read()
print(message)
