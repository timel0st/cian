import requests

from bs4 import BeautifulSoup
from write_csv import write_csv, write_one_csv
from fake_headers import Headers
#from get_page_text import web
headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15"
    }

header = Headers(
        # generate any browser & os headeers
        headers=False  # don`t generate misc headers
    )

def parse_one_page(url):
    # 1
    req = requests.get(url, headers=header.generate())
    # print(req.url)
    print(req.status_code)
    soup = BeautifulSoup(req.text, 'lxml')

    #2
    # src = web(url)
    # # print(src)
    # soup = BeautifulSoup(src[0], 'lxml')


    # find_text = soup.find("div", text="Объявление снято с публикации")
    # print(find_text)
    adress = ''
    # while adress == '' or adress == '-':
    #     try:
    #
    #         # adress_row = soup.find_all('a', class_='a10a3f92e9--address--SMU25')
    #         # #print(adress_row)
    #         # for iteam in adress_row:
    #         #     adress += f'{iteam.text}, '
    #         # adress = adress.strip()[:-1]
    #         adress = soup.find('div', class_='a10a3f92e9--address-line--GRDTb').find_parent().find_parent().text
    #         # print(adress)
    #         adress = adress.split('На карте')[0]
    #     except:
    #         adress = '-'
    #     print(adress)

    try:

        # adress_row = soup.find_all('a', class_='a10a3f92e9--address--SMU25')
        # #print(adress_row)
        # for iteam in adress_row:
        #     adress += f'{iteam.text}, '
        # adress = adress.strip()[:-1]
        adress = soup.find('div', class_='a10a3f92e9--address-line--GRDTb').find_parent().find_parent().text
        # print(adress)
        adress = adress.split('На карте')[0]
    except:
        adress = '-'
    print(adress)



    name = soup.find('h1').text
    print(name)
    try:
        square = soup.find('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_6u--A1GMI a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG').text
    except:
        square = '-'
    print(square)
    try:
        type = soup.find('span', class_='a10a3f92e9--value--Y34zN').text
    except:
        type = '-'
    print(type)
    try:
        price_row = soup.find('div', class_='a10a3f92e9--price--PcAEt').find('span').find('span').text
        price = price_row.split('₽')[0].replace(' ', '')
    except:
        price = '-'
    print(price)

    url_new = req.url
    #url_new = src[1]
    print(url_new)

    #write_one_csv(name, price, square, adress, type, url_new)


