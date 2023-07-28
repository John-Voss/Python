from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

from selenium.webdriver.chrome.service import Service
service = Service('path/to/chromedriver.exe')
service.start()

browser = webdriver.Chrome(service=service)
start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'

browser.get(start_url)
time.sleep(10)

planets_data = []

def scrape():
    for i in range(1,2):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            current_page_num = int(soup.find_all('input', attrs={'class', 'page_num'})[0].get('value'))
            
            if current_page_num < i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
        
        for ul_tag in soup.find_all('ul', attrs={'class', 'exoplanet'}):
            li_tags = ul_tag.find_all('li')
            
            temp_list = []
            
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
                        
            hyperlink_litag = li_tags[0]
            temp_list.append('https://exoplanets.nasa.gov' + hyperlink_litag.find_all('a', href=True)[0]['href'])
            planets_data.append(temp_list)
        
        browser.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
        

scrape()

headers = ['Name', 'Light_years_from_Earth', 'Planet_mass', 'Stellar_magnitude','Discovery_date', 'Hyper_link']
planet_df1 = pd.DataFrame(planets_data, columns=headers)
planet_df1.to_csv('updated_scraped_data.csv', index=True, index_label='id')