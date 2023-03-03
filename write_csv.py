import csv

def write_csv():
    with open('cian.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Название',
                'Цена',
                'Площадь',
                'Адрес',
                'Тип',
                'Ссылка'
            )
        )

def write_one_csv(name, price, square, adress, type, url):
    with open('cian.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                name,
                price,
                square,
                adress,
                type,
                url
            )
        )


