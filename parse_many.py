import time
from parse_one_page import parse_one_page

new_url = 'https://www.cian.ru/sale/flat/'


def parse():
    i = 280994721
    while True:
        url = new_url + f'{i}/'
        print(i)
        # response = requests.get(url)
        # print(response.status_code)

        parse_one_page(url)

        # print(response.url)
        # print(response.text)
        i += 1
        time.sleep(5)


