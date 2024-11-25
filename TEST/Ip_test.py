import requests

def get_ip_info():
    ip = requests.get('https://api.ipify.org').text
    if 163.198 in ip: 
        country = 'RUS'
        flag = NL.png
    return ip, country

ip, country = get_ip_info()

print(f'IP-адрес: {ip}')
print(f'Страна: {country}')
print(f'Флаг: {flag}')

