import httplib2

http = httplib2.Http()

url = 'https://jsonplaceholder.typicode.com/posts/1'
response, content = http.request(url, 'GET')
print(content)
