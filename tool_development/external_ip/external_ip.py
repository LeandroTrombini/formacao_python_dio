import requests

response = requests.get('https://ipinfo.io/json')

data = response.json()

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print('Detalhes do seu IP externo\n')
print(f'IP: {ip}\nRegion: {region}\nCountry: {country}\nOrg: {org}\nCity: {city}\n')