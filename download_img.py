
import time
import urllib.request



nbr_err = 0
nbr_dow = 0
with open('produit_sup.csv','r') as line:
    with open('image_non_telecharger.csv','w') as fich:

        for ind, i in enumerate (line) :
            li = i.split(';')
            nom ='images\\'+li[0]+".jpg"
            
            try:

                urllib.request.urlretrieve(li[3],nom)
                print('Image N:'+str(ind)+' Téléchargée ............')
                nbr_dow += 1
            except:
                nbr_err += 1
                line_error = [li[0],li[3]]
                line_error = ';'.join(line_error)
                fich.write(line_error+'\n')
                print('Image N:'+str(ind)+' Non téléchargée ............')            
            
print('Le téléchargement des images est términé avec '+str(nbr_dow)+' importé et '+str(nbr_err)+' échooué')
