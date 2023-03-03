import requests

#url = 'https://www.cian.ru/rent/flat/280998892/'

url = 'https://www.cian.ru/sale/flat/280994651/'

new_url = 'https://www.cian.ru/sale/flat/'

def parse():
    for i in range(280994651, 280994661):
        url = new_url + f'{i}/'
        response = requests.get(url)
        print(response.status_code)
        print(response.url)
        #print(response.text)

if __name__ == '__main__':
    parse()