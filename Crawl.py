import requests
from bs4 import BeautifulSoup
url = "https://xe.chotot.com/mua-ban-o-to"
response = requests.get(url)

if response.status_code == 200:
	print("Request Successfully!")
	#html_content = response.text
	soup = BeautifulSoup(response.text, 'html.parser')
	info = soup.find_all('div', role='button')

	if(info):
		with open('otoChoTot.txt', 'a',encoding='utf-8') as f:
			for car in info:
				name = car.find('h3', class_='adonovt')
				name_text = name.text.strip() if name else "N/A"
				price = car.find('span', class_='bfe6oav')
				price_text = price.text.strip() if price else "N/A"
				link = car.find('a', itemprop='item')
				print("SP: "+ name_text +"\nGia: "+ price_text +"\n -> https://xe.chotot.com"+link.get('href')+"\n")
				f.write("SP: "+ name_text +"\nGia: "+ price_text +"\n -> https://xe.chotot.com"+link.get('href')+"\n")
	else: print("no")
else:
    print("Request Failed", response.status_code)