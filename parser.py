from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import url_ozon
import bs4
import selenium
from bs4 import BeautifulSoup
import pandas as pd
rate1 = list()
rate2= list()
rate3 = list()
rate4 = list()
rate5 = list()
main_rate = list()
brand = list()
ids = list()
objects = list()
urls = list()


def get_page_ozon(URL):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    response = driver.get(url=URL)
    html = driver.page_source

    return html

def get_data(URL):
    soup = BeautifulSoup(get_page_ozon(URL=URL), "html.parser")
    rates = soup.find_all("div",{"class":"ui-d0a"})
    x = 0
    mr = soup.find('div',{"class":"w5w"}).find('span').get_text()
    br = soup.find('dd',{"class":"r3l"})
    for obj in rates:
        if x != 5:
            rate = str(obj)
            rate.replace('<div class="ui-d0a" style="width:','').replace('%;"></div>','')
            data = rate.replace('<div class="ui-d0a" style="width:','').replace('%;"></div>','')
            x = x+1
            objects.append(data)
            print(objects)

        else:
            break
        print(objects)
        rate1.append(objects[0])
        rate2.append(objects[1])
        rate3.append(objects[2])
        rate4.append(objects[3])
        rate5.append(objects[4])
        main_rate.append(mr)
        brand.append(br)
        ids.append('0')
        urls.append(URL)

def save_data_ozon(brand,ids,urls,rate1,rate2,rate3,rate4,rate5,main_rate):

    df = pd.DataFrame({"brands":brand,
                       "ids":ids,
                       "urls":urls,
                       "rate1":rate1,
                       "rate2":rate2,
                       "rate3":rate3,
                       "rate4":rate4,
                       "rate5":rate5,
                       "main_rate":main_rate

                       })


    writer = pd.ExcelWriter(f'ozon.xlsx', engine='xlsxwriter')
    df.to_excel(writer,sheet_name="ozon",index=False)
    writer.close()


get_data(URL='https://www.ozon.ru/product/flyaga-decathlon-quechua-500-bordovyy-244569915/reviews/?sort=created_at_desc')


