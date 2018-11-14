import smtplib


import requests
from lxml import html
from lxml import etree

page = requests.get('https://et.wikipedia.org/wiki/Vikipeedia:N%C3%A4dala_artiklid_2018')
tree = html.fromstring(page.content)

list = ['//*[@id="mw-content-text"]/div/p[6]/b/a', '//*[@id="mw-content-text"]/div/p[9]/b/a', '//*[@id="mw-content-text"]/div/p[14]/b/a', '//*[@id="mw-content-text"]/div/p[19]/b/a', '//*[@id="mw-content-text"]/div/p[24]/b/a', '//*[@id="mw-content-text"]/div/p[31]/b/a', '//*[@id="mw-content-text"]/div/p[35]/b/a', '//*[@id="mw-content-text"]/div/p[38]/b/a', '//*[@id="mw-content-text"]/div/p[42]/b/a', '//*[@id="mw-content-text"]/div/p[45]/b/a', '//*[@id="mw-content-text"]/div/p[48]/b/a', '//*[@id="mw-content-text"]/div/p[50]/b/a', '//*[@id="mw-content-text"]/div/p[53]/b/a', '//*[@id="mw-content-text"]/div/p[56]/b/a', '//*[@id="mw-content-text"]/div/p[59]/b/a', '//*[@id="mw-content-text"]/div/p[62]/b/a', '//*[@id="mw-content-text"]/div/p[66]/b/a', '//*[@id="mw-content-text"]/div/p[72]/b/a', '//*[@id="mw-content-text"]/div/p[74]/b/a', '//*[@id="mw-content-text"]/div/p[77]/b/a', '//*[@id="mw-content-text"]/div/p[83]/b/a', '//*[@id="mw-content-text"]/div/p[86]/b/a', '//*[@id="mw-content-text"]/div/p[88]/b/a', '//*[@id="mw-content-text"]/div/p[93]/b/a', '//*[@id="mw-content-text"]/div/p[97]/b/a', '//*[@id="mw-content-text"]/div/p[100]/b/a', '//*[@id="mw-content-text"]/div/p[103]/b/a', '//*[@id="mw-content-text"]/div/p[106]/b/a', '//*[@id="mw-content-text"]/div/p[110]/b/a', '//*[@id="mw-content-text"]/div/p[113]/b/a', '//*[@id="mw-content-text"]/div/p[117]/b/a', '//*[@id="mw-content-text"]/div/p[119]/b/a', '//*[@id="mw-content-text"]/div/p[125]/b/a', '//*[@id="mw-content-text"]/div/p[128]/b/a', '//*[@id="mw-content-text"]/div/p[132]/b/a', '//*[@id="mw-content-text"]/div/p[135]/b/a', '//*[@id="mw-content-text"]/div/p[140]/b/a', '//*[@id="mw-content-text"]/div/p[140]/b/a', '//*[@id="mw-content-text"]/div/p[144]/b/a', '//*[@id="mw-content-text"]/div/p[148]/b/a', '//*[@id="mw-content-text"]/div/p[151]/b/a', '//*[@id="mw-content-text"]/div/p[155]/b/a', '//*[@id="mw-content-text"]/div/p[159]/b/a', '//*[@id="mw-content-text"]/div/p[164]/b/a', '//*[@id="mw-content-text"]/div/p[167]/b/a', '//*[@id="mw-content-text"]/div/p[171]/b/a']
linkide_kogu = []

for i in range(len(list)):
    for a in tree.xpath(list[i]):
        kogu_sisu = (etree.tostring(a, method='html', with_tail=False))
    
    kogu_sisu = str(kogu_sisu.split()[1]).split('"')
    linkide_kogu.append("https://et.wikipedia.org/"+ kogu_sisu[1])

#print(linkide_kogu)



#loe_edasi = tree.xpath('//*[@id="mw-content-text"]/div/p[6]/b/a/text()')
#
#if tree.xpath('//*[@id="mw-content-text"]/div/p[6]/b/a/text()') == loe_edasi:      
#    for a in tree.xpath('//*[@id="mw-content-text"]/div/p[6]/b/a'):
#        kogu_sisu = (etree.tostring(a, method='html', with_tail=False))
#
#    kogu_sisu = str(kogu_sisu.split()[1]).split('"')
#
#    link = "https://et.wikipedia.org/"+ kogu_sisu[1]
#    print(link)
#else:
#    print("shallalalalla")
    
    

#for i in range(100):
#    sidrun = "'//*[@id=\"mw-content-text\"]/div/p[" + str(i) + "]/b/a/text()'" #selle reaga on probleem (' ja " kasutamine)
#    print(sidrun)
#    apelsin = tree.xpath(sidrun)
#    print(apelsin)
#    
#    if apelsin == apelsin: #loe_edasi:      
#        for a in tree.xpath(sidrun):
#            kogu_sisu = (etree.tostring(a, method='html', with_tail=False))
#
#        kogu_sisu = str(kogu_sisu.split()[1]).split('"')
#
#        link = "https://et.wikipedia.org/"+ kogu_sisu[1]
#        print(link)
#    else:
#        #print("pole midagi/ei töötra")'
#        continue

#nädal=tree.xpath(
#    '//*[@id="mw-content-text"]/table/tr/td[2]/a[1]/text()')
#töötav versioon

#aadress = tree.xpath(
#    '//*[@id="mw-content-text"]/div/p[165]/b/a[starts-with(@href,"/wiki")]') 
#print(aadress)
#returns bynary?orsm

#aadress = tree.xpath(
#    '//*[@id="mw-content-text"]/div/p[165]/b/a/title') 
#print(aadress)
#print(aadress.text)


#koodijupp saadud lehelt: http://naelshiab.com/tutorial-send-email-python/
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("hexagonal300@gmail.com", "pallimeri")
 
msg = str(link)
server.sendmail("hexagonal300@gmail.com", "trolololobro@gmail.com", msg)
server.quit()