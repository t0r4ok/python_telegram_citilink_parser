import requests
from bs4 import BeautifulSoup

url = 'https://www.citilink.ru/catalog/videokarty/'
r = requests.get(url)


def parse_videocart(name):
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

                    scan = soup.find_all("div", class_="product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist")

                    for e in scan:
                        data_params = e.get('data-params')
                        elements.append(
                            {
                                'name': e.find('a', class_="ProductCardHorizontal__title  Link js--Link Link_type_default").get_text(strip=True)
                            }
                        )

        except:
            continue
    print(elements)
    table_video_cart = " ".join([i for i in url_cart if name in i])
    return table_video_cart if len(table_video_cart) > 0 else "Данная видеокарта отсутствует "
