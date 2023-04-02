#test
#url = 'https://www.cian.ru/rent/flat/280998896/'
#
#url = 'https://www.cian.ru/sale/flat/280994651/'
url = 'https://www.cian.ru/sale/flat/280994662/'
# new_url = 'https://www.cian.ru/sale/flat/'
#
# def parse():
#     for i in range(280994651, 280994661):
#         url = new_url + f'{i}/'
#         response = requests.get(url)
#         print(response.status_code)
#         print(response.url)
#         #print(response.text)

from parse_many import parse
from parse_one_page import parse_one_page
from write_csv import write_csv
# aioreq
# нужно дату обьявления парсить!!!

headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15"
    }




if __name__ == '__main__':
    #parse_one_page(url)
    #write_csv()
    #write_one_csv()

    parse()


