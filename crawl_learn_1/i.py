import requests
from bs4 import BeautifulSoup

with open('rdsd.txt', 'r') as file:
    # Đọc từng dòng và in ra màn hình
    for line in file:
        try:
            soup = BeautifulSoup(requests.get("https://www.facebook.com/{}".format(line.strip())).text, 'html.parser')
            hhh = soup.find("meta", {'content': lambda x: x and 'đang ở trên ' in x.lower()})
            clm = hhh.get('content')
            print(clm + '\n')
        except:
            print(line.strip() + '\n')
            continue
