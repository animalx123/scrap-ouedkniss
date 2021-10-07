from bs4 import BeautifulSoup
from maps_rewars_restaurant import scraping_map

#Récuperation de la data global
infos_data =scraping_map()

adr = infos_data['adresse']
num = infos_data['num']
note = infos_data['note_global']
hor = infos_data['horaires']
nom_resto = infos_data['nom_resto']



with open('test_com.html','w',encoding='utf-8') as f :

    #Parcourire tout les commentaires
    com = infos_data['rewards']
    for i in com :
        username = i[0]
        info_user = i[1]
        commentaire = i[2]
        note_user = i[3]
        try:
            liens_images = i[4]
        except:
            pass
    
        el = '''<div>
        <h4>{username}</h4>
        <h6>{info_user}</h6>
        <h4>{note_user}</h4>
        <p>{commentaire}</p>
        </div></br>'''.format(username = username,note_user = note_user,commentaire = commentaire,info_user = info_user)

        f.write(el)




    
    
   


'''with open('result_html_resto.html','r+') as f :
    soup = BeautifulSoup(f,'html.parser')
    soup.find('h4',{'id':'adresse'}).string = 'Adresse : El Harrach'
    soup.find('h4',{'id':'tel'}).string = 'Téléphone : +213542698744'
    soup.find('h4',{'id':'note'}).string = 'Note : 4,2'

    f.seek(0)
    f.write(str(soup))
    '''