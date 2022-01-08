import requests

city = input('Enter the name of the city you according to your wish : ')
print(city)

print('\nDisplaying weather report for : '+city)

url = 'https://wttr.in/{}'.format(city)
res=requests.get(url)

print(res.text)