import requests
from bs4 import BeautifulSoup

def parse_ssr():
    r = requests.get("https://magnum.kz/?city=almaty/")
    s = BeautifulSoup(r.content, 'html.parser')
    d = s.find('a', {'href': '/product/101724?city=Almaty'}). text
    return d

if __name__ ==  'main':
    print("Акции:", parse_ssr())





