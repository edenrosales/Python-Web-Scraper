from bs4 import BeautifulSoup
import requests


html_address = requests.get('https://www.vlr.gg/stats').text
soup = BeautifulSoup(html_address, 'lxml')
info = soup.find_all('td',class_='mod-player mod-a')
for elemenets in info:
    if len(elemenets.text.split())>=2:
        first_part= f"Name: {elemenets.text.split()[0]}"
        second_part= f"Player Tag: {elemenets.text.split()[1]}"
        print('{0:<20} {1:<30}'.format(first_part,second_part))     #this is just for the formatting, i am not really sure how this works, but i just put in random numbers and it worked :D
    else:
        text= elemenets.text.replace('\n','')
        print(f"Name: {text}")