# C:\Users\#####\AppData\Local\Programs\Python\Python313>
# pip install requests
# Realizar peticiones HTTP
#
# pip install beautifulsoup4
# https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-find/
# Extraer contenido de ficheros html y XML
# https://www.geeksforgeeks.org/python-web-scraping-tutorial/

import requests
from bs4 import BeautifulSoup

req = requests.get('https://tearium.es/')

# respuesta del servidor
# print(req)

# Imprime el contenido siempre que sea accesible
# print(req.content)

contenido = BeautifulSoup(req.content, 'html.parser')

# Mostramos la web organizada
# print(contenido.prettify())

s = contenido.find_all('h3', class_='product-title')
# content = contenido.find_all('a')
# print(s)

for product in contenido.find_all('h3', class_='product-title'):
    print(product.text)
