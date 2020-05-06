import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
wepage = requests.get('https://www.mygov.in/covid-19')
soup = BeautifulSoup(wepage.content,'html.parser')
nstr = soup.select(".st_name") 
namestr = []
for i in nstr:
    stri = str(i)
    striu = stri[22:-7]
    namestr.append(striu)
# print(namestr)                                   # ultimate names   
# namestr is ultimate list of names
dati = soup.select(".info_title")
strdati = str(dati[0]) 
print(strdati[57:-14])                           #ultimate date and time
snamelst = [i[:3] for i in namestr]
nustr = soup.select(".st_number")
numstr = []
for i in nustr:
    strn = str(i)
    strnu = strn[24:-7]
    numstr.append(int(strnu))
# print(numstr)                                    #ultimate numbers
#numstr is ultimate list of numbers
dadict = dict(zip(namestr,numstr))
print(dadict)                                  # ultimate dictionary 
plt.bar(snamelst,numstr)
plt.show()
plt.barh(snamelst,numstr)
plt.show()
plt.plot(snamelst,numstr)
plt.show()                                     
plt.scatter(snamelst,numstr)
plt.show()
plt.pie(numstr,explode=None,labels=snamelst)
plt.show()
a = input()    
