
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome('chromedriver.exe')

url = "https://www.google.fr/maps/place/Le+D%C3%B4me/@36.7599077,3.1365536,12z/data=!4m9!1m2!2m1!1srestaurants!3m5!1s0x128fad5b6817bfdf:0xfda18ed1f67a65ad!8m2!3d36.7328767!4d3.0835718!15sCgtyZXN0YXVyYW50c1oNIgtyZXN0YXVyYW50c5IBCnJlc3RhdXJhbnQ"
driver.get(url)

driver.implicitly_wait(8)

#récupération infos du restaurant
resto  = driver.find_element_by_tag_name('h1')
print(resto.text)
infos = driver.find_elements_by_xpath('//button[@class="CsEnBe"]')
for info in infos:
    label = info.get_attribute('aria-label')
    if label != None and 'Adresse' in label:
        print(label)
    if label != None and 'Numéro de téléphone' in label:
        print(label)

#Note génerale du restorant
note = driver.find_element_by_class_name('gm2-display-2').text
print(note)

#Récupérer les horaires du restaurant
horaires = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[9]/div[2]/div[2]').get_attribute('aria-label')
print(horaires)

#aller au boutton PLUS D'AVIS
loc = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[36]/div/button')
ActionChains(driver).move_to_element(loc).perform()

time.sleep(3)
#Aller dans tout les avis
driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[36]/div/button').click()
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
for item in item_reward:

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


    #print("*  ",user.text,"  ",info_user_ar,"   ",txt.text,"       ",etoiles)
    #print(liens_images)
    liens_images =[]


print("==========================================")

        







