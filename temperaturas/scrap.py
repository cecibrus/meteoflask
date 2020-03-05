import requests
from bs4 import BeautifulSoup

#Primero que nada, se cargan las URLs correspondientes a cada ciudad para poder extraer los datos de acuerdo a cada una
asuncion='https://www.meteored.com.py/tiempo-en_Asuncion-America+Sur-Paraguay-Central--1-22742.html'
concepcion_b= 'https://www.meteored.com.py/tiempo-en_Belen-America+Sur-Paraguay-Concepcion--1-22836.html'
san_pedro='https://www.meteored.com.py/tiempo-en_San+Pedro-America+Sur-Paraguay-San+Pedro--1-22925.html'
caacupe='https://www.meteored.com.py/tiempo-en_Caacupe-America+Sur-Paraguay-Cordillera--1-22728.html'
villarrica='https://www.meteored.com.py/tiempo-en_Villarrica-America+Sur-Paraguay-Guaira--1-22741.html'
cnel_oviedo='https://www.meteored.com.py/tiempo-en_Coronel+Oviedo-America+Sur-Paraguay-Caaguazu--1-22738.html'
caazapa='https://www.meteored.com.py/tiempo-en_Caazapa-America+Sur-Paraguay-Caazapa--1-22889.html'
encarnacion='https://www.meteored.com.py/tiempo-en_Encarnacion-America+Sur-Paraguay-Itapua--1-22959.html'
san_juan='https://www.meteored.com.py/tiempo-en_San+Juan+Bautista-America+Sur-Paraguay-Misiones--1-22891.html'
paraguari='https://www.meteored.com.py/tiempo-en_Paraguari-America+Sur-Paraguay-Paraguari--1-22740.html'
ciudad_del_este='https://www.meteored.com.py/tiempo-en_Ciudad+del+Este-America+Sur-Paraguay-Alto+Parana--1-22739.html'
aregua='https://www.meteored.com.py/tiempo-en_Aregua-America+Sur-Paraguay-Central--1-22729.html'
pilar='https://www.meteored.com.py/tiempo-en_Pilar-America+Sur-Paraguay-Neembucu--1-22890.html'
pedro_juan_caballero='https://www.meteored.com.py/tiempo-en_Pedro+Juan+Caballero-America+Sur-Paraguay-Amambay--1-22839.html'
salto_del_guaira='https://www.meteored.com.py/tiempo-en_Salto+del+Guaira-America+Sur-Paraguay-Canindeyu--1-22916.html'
villa_hayes='https://www.meteored.com.py/tiempo-en_Villa+Hayes-America+Sur-Paraguay-Presidente+Hayes--1-22735.html'
filadelfia='https://www.meteored.com.py/tiempo-en_Filadelfia-America+Sur-Paraguay-Boqueron--1-22840.html'
fuerte_olimpo='https://www.meteored.com.py/tiempo-en_Fuerte+Olimpo-America+Sur-Paraguay-Alto+Paraguay--1-22690.html'

#luego se pone en una lista para poder recorrerla con facilidad 
ciudades=[asuncion,concepcion_b,san_pedro,caacupe,villarrica,cnel_oviedo,caazapa,encarnacion,san_juan,paraguari,ciudad_del_este,aregua,pilar,pedro_juan_caballero,salto_del_guaira,villa_hayes,filadelfia,fuerte_olimpo]

#aqui se crean listas vacias donde se iran cargando los distintos datos, en el mismo orden que las URLs
#para luego poder acceder a ellos cuando sea necesario simplemente con el indice de la ciudad en la lista
temperaturas=[]
velocidades=[]
direcciones=[]
lis_ciudades=[]

for x in ciudades: 
    page=requests.get(x) #se obtiene la pagina de acuerdo a la lista
    soup=BeautifulSoup(page.content,'html.parser')

    #se extraen los datos de temperatura
    temp=soup.find_all("span", class_="dato-temperatura changeUnitT")
    temp=temp[0].get_text()
    temperaturas.append(temp) #se agrega a la lista de temperaturas

    #se repite el mismo proceso que con las temperaturas para el resto de los datos
    viento=soup.find_all("span", class_="velocidad")
    viento=viento[0].get_text()
    velocidades.append(viento)

    direcc=soup.find_all("span", class_="datos-viento")
    direcc=direcc[0].get_text()
    #en el caso de la direccion, trae unos datos adicionales, por lo que se debe recortar la cadena
    espacio=direcc.find(" ",4) #se busca el primer espacio desde el 5to caracter para poder saber donde cortar la cadena
    direcc=direcc[:espacio] #y aqui se corta la cadena a fin de tener solo la direccion del viento
    direcciones.append(direcc)

    ciudad=soup.find_all("h1", class_="titulo")
    ciudad=ciudad[0].get_text()
    lis_ciudades.append(ciudad)








