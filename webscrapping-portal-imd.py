# -- coding: utf-8 --
"""
Created on Sun Jan 20 16:24:33 2019

@author: tauab
"""
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
import psycopg2

url = 'https://www.imd.ufrn.br/portal/noticias'
webPage = urlopen(url)
pageHTML = webPage.read()
webPage.close()

page_soup = bs(pageHTML, "html.parser")

conn = psycopg2.connect(host="host",database="db", user="user", password="password")
cursor = conn.cursor()
cursor.execute("TRUNCATE valores_banco_newsmodel")
cartoes_texto = page_soup.findAll("div", {"class":"card-block p-2"})

listaTituloCartao = []
listaTextoCartao = []
listaDataCartao = []

for cartaoDummy in cartoes_texto:
    listaTituloCartao.append(cartaoDummy.h4.text)
    listaTextoCartao.append(cartaoDummy.p.text)
    listaDataCartao.append(cartaoDummy.div.text.split('\n')[1].split('por')[0])

for i in range (0, len(listaTituloCartao)):
    cursor.execute("INSERT INTO valores_banco_newsmodel(title, text, date) VALUES (%s, %s, %s)", 
                   (listaTituloCartao[i], listaTextoCartao[i], listaDataCartao[i]))
conn.commit()
