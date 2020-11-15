import requests
from bs4 import BeautifulSoup

url = 'https://mp.weixin.qq.com/s/7qgz2PNaUxcf-WxUzzbf5A'
response = requests.get(url=url)

# print(response.text)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
imgs = soup.find_all('img')

print(imgs)

# enumerate is to assign no. to images
for i, img in enumerate(imgs):
    # print(img.get('data-src'))
    image_url = img.get('data-src')

    # if image_url exists, get the image using .content and save it in ./pic/
    if image_url:
        response = requests.get(url=image_url)
        with open('./pic/{}.jpg'.format(i), 'wb') as f:
            f.write(response.content)
            print('Saved image {}'.format(i))