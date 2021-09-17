from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome('chromedriver.exe')

urls=[]
cond = True
nb_page = 1

#Récole des liens avec la pagination
while cond :

    driver.get("https://www.ouedkniss.com/automobiles/"+str(nb_page))

    auto = driver.find_elements_by_class_name('annonce_titre')

    for i in auto:

        urls.append(i.find_element_by_tag_name('a').get_property('href'))
        
    print('page '+ str(nb_page)+'  fini.....................')

    nb_page+=1

    if nb_page == 50:

        cond = False
    
    
print(len(urls))


#Recuperation des informations et création du fichier csv 
with open('offres_voitures.csv','w',encoding='utf-8') as line:

    for ind,i in enumerate(urls):

        driver.get(i)

        img_404= driver.find_element_by_id('page').find_element_by_id('page_contenu')

        if img_404.find_element_by_tag_name('h1').text == "Page n'existe plus" :

            print('N:'+ str(ind+1) +"lien mort ...............")

            pass

        else:

            try:

                titre = driver.find_element_by_id('Title').text

            except:

                titre=''

            try:

                desc = driver.find_element_by_id('Description')
                type_v = desc.find_element_by_id('Catégorie').text[18:]
                moteur = desc.find_element_by_id('Moteur').text[8:] 
                kilometre = desc.find_element_by_id('Kilométrage').text[12:] 
                couleur = desc.find_element_by_id('Couleur').text[9:] 
                energie = desc.find_element_by_id('Energie').text[9:] 
                phone = driver.find_element_by_id('direct_call').find_element_by_tag_name('a').get_property('href')[4:]
            
            except:

                pass

            try:

                eprix = driver.find_element_by_id('Prix').find_element_by_tag_name('span').text

            except:

                eprix=''

            try:

                email = driver.find_element_by_class_name('Email').find_element_by_tag_name('a').text

            except:

                email=''
            
            try:

                adresse = driver.find_element_by_class_name('Adresse').text
            
            except:

                adresse =''

            if  driver.find_elements_by_id('store'):

                infos_name = driver.find_element_by_id('store_name').text #annonceur avec store

            else:

                infos_name = driver.find_element_by_id('Annonceur').find_element_by_tag_name('a').text #annonceur normal

            li = [titre,type_v,moteur,kilometre,couleur,energie,eprix,adresse,email,phone,infos_name]

            li=';'.join(li)
            
            try:

                line.write(li+'\n')

                print('N:'+ str(ind+1) +' Ajouté ......')
                
            except:

                line.write(''+'\n')

                print('N:'+ str(ind+1)+' ligne ignorée .....................................')

driver.quit()
driver.close()
    
    
    
        

