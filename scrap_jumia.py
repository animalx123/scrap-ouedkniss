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


urls=[]
cond = True
nb_page = 1



start_time = time.perf_counter()
print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
print('Récolte de liens en cour #-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')


with open('produits_supermarché.csv','w') as line:
    count_article = 1

    while cond :

        driver.get("https://www.jumia.dz/mlp-epicerie/epicerie/?page="+str(nb_page)+"#catalog-listing")

        #Condition pour fermé la Popup
        try:

            if driver.find_element_by_css_selector('#pop > div > section > div'):
                driver.find_element_by_css_selector('#pop > div > section > button').click()
        except:
            pass

        auto = driver.find_elements_by_class_name('core')
        
        print('il ya '+str(len(auto))+' dans cette page ...................')
        
        for ind,i in enumerate (auto):

            image = i.find_element_by_class_name('img-c').find_element_by_tag_name('img').get_attribute('data-src')
            nom = i.find_element_by_class_name('info').find_element_by_class_name('name').text
            prix = i.find_element_by_class_name('info').find_element_by_class_name('prc').text

            li = [nom,prix,image]
            li=';'.join(li)
            try:

                line.write(li+'\n')
                print('Ligne N:'+ str(ind+1) +' Ajouté  ......')
                count_article += 1
                
            except:
                
                print('Ligne N:'+ str(ind+1) +' Ignorée  ......')

            
        print('Page N: '+ str(nb_page)+' Terminé.......... '+str(count_article)+' articles récolté ......')

        nb_page+=1

        if nb_page == 44:

            cond = False
        


    print(str(len(urls)) + ' urls en '+ str(temp_ecoule(start_time)))