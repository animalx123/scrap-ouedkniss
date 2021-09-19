from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome('chromedriver.exe')

def temp_ecoule(debut):

    timeX = round(((time.perf_counter() - debut)/60),2)
    hours, seconds = divmod(timeX * 60, 3600)
    minutes, seconds = divmod(seconds, 60)
    return  "{:02.0f}:{:02.0f}:{:02.0f}".format(hours, minutes, seconds)


urls_cats =[]

driver.get("https://superetti.dz/")

#Récolte liens de categories
cat = driver.find_element_by_id('menu-categories').find_elements_by_tag_name('li')

for i in cat:

    urls_cats.append(i.find_element_by_tag_name('a').get_property('href'))



#parcourir la pagination des categories


for ind_cat, lien_categorie in enumerate(urls_cats):

    cond = True
    nb_page = 1
    
    while cond :

        driver.get(lien_categorie+'/page/'+str(nb_page)+'/')


        nb_page += 1

        try:
            if  driver.find_element_by_css_selector('#modal-ready > div > div > div > section > div > div > div.elementor-column.elementor-col-66.elementor-top-column.elementor-element.elementor-element-7301229 > div > div > div.elementor-element.elementor-element-3742262.elementor-widget.elementor-widget-wd_title > div > div > div.liner-continer > h4'):
                print('404  détecter.....................................')
                cond = False
        except:
            print('404 non détecter ........................................')

            
