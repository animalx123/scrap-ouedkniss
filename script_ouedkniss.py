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

#Récole des liens avec la pagination
start_time = time.perf_counter()
print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
print('Récolte de liens en cour #-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
while cond :

    driver.get("https://www.ouedkniss.com/automobiles/"+str(nb_page))

    auto = driver.find_elements_by_class_name('annonce_titre')
    link_count = 0
    for i in auto:
        
        urls.append(i.find_element_by_tag_name('a').get_property('href'))
        link_count += 1
        
    print('Page N: '+ str(nb_page)+' Terminé.......... '+str(link_count)+' Liens récolté ......')

    nb_page+=1

    if nb_page == 2:

        cond = False
    


print(str(len(urls)) + ' urls en '+ str(temp_ecoule(start_time)))


#Recuperation des informations et création du fichier csv 
print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
print('Récole d informations et écriture du fichier en cour #-#-#-#-#-#-#-#-#-#-#-#-#-#-# ')
print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
nbr_line = 1
with open('offres_voitures.csv','w') as line:
    start_time = time.perf_counter ()

    line.write('Titre;Date;Heure;Email;Telephone;Adresse;Nom;Type de voiture;Moteur;Kilométrage;Couleur;Energie;Prix' +'\n')
    for ind,i in enumerate(urls):

        driver.get(i)

        img_404= driver.find_element_by_id('page').find_element_by_id('page_contenu')

        if img_404.find_element_by_tag_name('h1').text == "Page n'existe plus" :

            print('Lien N:'+ str(ind+1) +" Mort ...............")

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
                kilometre = desc.find_element_by_id('Kilométrage').text[13:] 
                couleur = desc.find_element_by_id('Couleur').text[9:] 
                energie = desc.find_element_by_id('Energie').text[9:] 
                phone = driver.find_element_by_id('direct_call').find_element_by_tag_name('a').get_property('href')[4:]

                date = driver.find_element_by_css_selector('#Description > p:nth-child(3) > span').text
                date = date.replace(' ','')
                d , h  = date.split('à')
            
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
            

            li = [titre,d,h,email,phone,adresse,infos_name,type_v,moteur,kilometre,couleur,energie,eprix]

            li=';'.join(li)
            
            try:

                line.write(li+'\n')

                nbr_line += 1

                print('Ligne N:'+ str(ind+1) +' Ajouté  ......')

                
                
            except:

                line.write(''+'\n')

                print('Ligne N:'+ str(ind+1)+' Ignorée .....................................')


print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
print(str(nbr_line)+'Annonces récolté en ........'+str(temp_ecoule(start_time)))
print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')


    
    
        

