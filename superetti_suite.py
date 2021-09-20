from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome('chromedriver.exe')

page ="https://superetti.dz/categorie-produit/produits-laitiers/page/12/"

driver.get(page)


items = driver.find_elements_by_css_selector('div.product-grid-item')
categorie = driver.find_element_by_class_name('entry-title').text

for i in items:
    
    titre = i.find_element_by_class_name('product-title').find_element_by_tag_name('a').text
    prix = i.find_element_by_class_name('price').find_element_by_tag_name('span').text
    image = i.find_element_by_class_name('product-element-top').find_element_by_tag_name('img').get_attribute('data-src')
    