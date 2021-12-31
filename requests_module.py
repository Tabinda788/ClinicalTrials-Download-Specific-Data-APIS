import requests

url = 'https://clinicaltrials.gov/api/query/full_studies?expr=heart+attack'

x = requests.get(url)

# print(x.text)
# print(x.headers)

# print(x.headers["Set-Cookie"])

# git = requests.get('https://api.github.com/user', auth=('user', 'password'))
# print(git.status_code)
# print(git.text)

# print(git.json())


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)


