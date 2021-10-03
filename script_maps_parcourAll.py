from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com/maps/search/Restaurants/@36.7338783,3.0867705,14z/data=!3m1!4b1')

links =[]
cond =True
count_link = 0

while cond:
    scrolling_element= driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]')
    for i in range(5):
        scrolling_element.send_keys(Keys.END)
        time.sleep(2)
    
    
    elements = driver.find_elements_by_class_name('V0h1Ob-haAclf')

    for ind,i in enumerate (elements):
        try:
            links.append(i.find_element_by_tag_name('a').get_property('href'))
            count_link += 1
            
            
        except:
            print('Lien N:'+str(ind)+' ignoré.................')
    print(str(count_link))
    count_link = 0
    if count_link != 100 :
        # pagination
        cli = driver.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]').click()
       
    else :
        cond =False
        

