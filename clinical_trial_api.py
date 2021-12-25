import requests


def download_result(filename, content):
  file = open('{}.xml'.format(filename), 'w')
  file.write(content)
  file.close()
  return True


url = "https://clinicaltrials.gov/api/query/full_studies?expr=heart+attack"

payload={}
headers = {
  'Cookie': 'CTOpts=Qihzm6CLCwL6zw5G6yUgzw-R98F5OR4PNDWl; Psid=vihzm6CLCwL6zw5G6yz3FQ7V9ghH0gFRxR4waBFHkR0y0gzqaR78xBCGCD8V'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.text
downloaded = download_result("full_studies", data)
print(downloaded)

