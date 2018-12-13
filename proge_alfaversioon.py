#Kui saadetud meilis esineb täpitähti, siis meili saatmise võimaldamiseks eemaldatakse neist täpid. Kui meilile tulnud link ei tööta, tasub esimese asjana
#üle kontrollida, kas mõne tähe asemel (lingis) ei peaks olema pigem täpitäht. Samuti asendatakse lingis esinevad koolonid sõnaga 'koolon', et oleks võimalik
#meil saata. 

import smtplib
import requests
from lxml import html
from lxml import etree

#parool = input("Sisesta parool: ")

page = requests.get('https://et.wikipedia.org/wiki/Vikipeedia:N%C3%A4dala_artiklid_2018')#lehekülg millelt tõmbab html-i alla
tree = html.fromstring(page.content)

linkide_kogu = []
#salvestab loe_edasi muutujasse "Loe edasi..." (millega hakkab hiljem teisi selliseid pathe otsima)
loe_edasi = tree.xpath('//*[@id="mw-content-text"]/div/p[6]/b/a/text()')

for i in range(240):#hakkab ükshaaval html-i ridu läbima
    teekond = '//*[@id=\"mw-content-text\"]/div/p[' + str(i) + "]/b/a/text()"
 
    if tree.xpath(teekond) == loe_edasi: #kui on samuti tekstiga loe edasi...:      
        for a in tree.xpath('//*[@id=\"mw-content-text\"]/div/p[' + str(i) + "]/b/a"):
            kogu_sisu = (etree.tostring(a, method='html', with_tail=False)) #salvestab muutujasse HTML-i reas oleva kogu koodi

        kogu_sisu = str(kogu_sisu.split()[1]).split('"') #sptitib html-i koodi 
        linkide_kogu.append("et.wikipedia.org/"+ kogu_sisu[1])#paneb täispika leheküljenime kokku (saame kätte lingid)
        
    else: #kui koodireas pole sobivat linki, siis võtab ette järgmise rea
        continue

link = linkide_kogu[-1] #saame viimase nädalaartikli lingi
#link = link.replace('ä','a')
#link = link.replace('õ','o')
#link = link.replace('ö','o')
#link = link.replace('ü','u')
#link = link.replace(':','KOOLON(kustuta see ning asenda ise kooloniga)')
parool = "StellaRiin2018"

#link = "Saadan wikipeedia viimase n2dalaartikli lingi" + link
#saadab meili
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("projektijaoks@gmail.com", parool)
 
server.sendmail("projektijaoks@gmail.com", "trolololobro@gmail.com", link)
server.quit()