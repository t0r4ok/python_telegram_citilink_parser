import requests
from bs4 import BeautifulSoup


def parse_videocart(name):
    url = 'https://www.citilink.ru/catalog/videokarty/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text , 'html.parser')
    url_cart = []
    elements = []

    for i in soup.find_all('a'):
        try:
            if '/product/videokarta' in i.get('href'):
                if 'www.citilink.ru/' not in i.get('href'):
                    url_cart.append(f"www.citilink.ru{i.get('href')}")
                else:
                    url_cart.append(i.get('href'))

                    scan = soup.find_all("div", class_=" ProductHeader js--ProductHeader")

                    for e in scan:
                        elements.append(
                            {
                                'name': e.find('h1', class_="Heading Heading_level_1 ProductHeader__title").get_text(
                                    strip=True
                                )
                            }
                        )
        except:
            continue
    print(elements)
    table_video_cart = " ".join([i for i in url_cart if name in i])
    return table_video_cart if len(table_video_cart) > 0 else "Данная видеокарта отсутствует "


