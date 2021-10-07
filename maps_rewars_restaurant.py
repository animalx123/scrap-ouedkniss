
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time



def scraping_map():
    final_data = {'rewards':{}}
    info_data = {}
    rewards_data_item = []
    rewards_data = {}
    driver = webdriver.Chrome('chromedriver.exe')
    url = "https://www.google.com/maps/place/Restaurant+Grilling/@36.7467085,3.0260003,14z/data=!4m9!1m2!2m1!1srestaurant!3m5!1s0x128fb276eec10633:0x4017ac538ff11a7c!8m2!3d36.7466627!4d3.043523!15sCgpyZXN0YXVyYW50WgwiCnJlc3RhdXJhbnSSAQpyZXN0YXVyYW50"
    driver.get(url)

    driver.implicitly_wait(8)

    #récupération infos du restaurant
    resto  = driver.find_element_by_tag_name('h1')

    final_data['nom_resto'] = resto.text
    
    infos = driver.find_elements_by_xpath('//button[@class="CsEnBe"]')
    for info in infos:
        label = info.get_attribute('aria-label')
        if label != None and 'Adresse' in label:

            final_data['adresse'] = label
            
        if label != None and 'Numéro de téléphone' in label:

            final_data['num'] = label
            

    #Note génerale du restorant
    note = driver.find_element_by_class_name('gm2-display-2').text
    final_data['note_global'] = note
    

    #Récupérer les horaires du restaurant
    horaires = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[9]/div[2]/div[2]').get_attribute('aria-label')
    final_data['horaires'] = horaires
    

    #aller au boutton PLUS D'AVIS
    buts = driver.find_elements_by_class_name('M77dve')
    for bu in buts:
        lab = bu.get_attribute('aria-label')
        if lab != None and "Plus d'avis" in lab:
            print(lab)
            ActionChains(driver).move_to_element(bu).perform()
            time.sleep(3)
            #Aller dans tout les avis
            bu.click()
            time.sleep(5)
    

    
    
    
    
    #Scroller dans la page 5 fois
    scrolling_element= driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]')
    for i in range(5):
        scrolling_element.send_keys(Keys.END)
        time.sleep(2)

    info_user_ar =[]
    liens_images =[]

    #récuperation des Rewards
    item_reward = driver.find_elements_by_class_name('ODSEW-ShBeI-content')
    for ind, item in enumerate(item_reward):   

        item_com =[]
        rewards_data = [] 

        #Récupérer liens des images si ils existent
        imgs = item.find_elements_by_class_name('ODSEW-ShBeI-Jz7rA')
        for im in imgs:
            urls_img = im.find_elements_by_tag_name('button')
            for url_img in urls_img:
                st =url_img.get_attribute('style')
                beg =st.find('background-image: url("') + len('background-image: url("')
                end = st.find('");')
                liens_images.append(st[beg:end])

        
        
        #récupérer le nom et les infos du user
        user = item.find_element_by_class_name('ODSEW-ShBeI-title').find_element_by_tag_name('span')
        info_user = item.find_elements_by_class_name('ODSEW-ShBeI-VdSJob')
        info_user_ar = []
        for iu in info_user:
            info_user_ar.append(iu.text)
  
        # afficher la suite du commentaire si il existe
        voir_plus = item.find_elements_by_tag_name('button')
        for v in voir_plus:
            if 'Voir plus' == v.get_attribute('aria-label'):
                v.click()

        #récupérer les rewards        
        txt = item.find_element_by_class_name('ODSEW-ShBeI-text')
        etoiles = item.find_element_by_class_name('ODSEW-ShBeI-H1e3jb').get_attribute('aria-label')

        item_com = [user.text,info_user_ar,txt.text,etoiles,liens_images]
        rewards_data_item.append(item_com)
        
        #final_data['infos'] = info_data
        final_data['rewards'] = rewards_data_item
        print('commentaire N: '+str(ind + 1)+' ajouté avec succes ....................................')
        #print("*  ",user.text,"  ",info_user_ar,"   ",txt.text,"       ",etoiles)
        #print(liens_images)
        liens_images =[]

    return final_data


    

    

        







