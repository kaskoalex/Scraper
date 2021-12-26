
1
2
3
import requests # Bibliothek wird importiert...
 
r = requests.get(' https://www.papagai.de/tour-plan/') # ... und kümmert sich von selbst um die Verbidung, auch https geht.
print(r.status_code)
#200 - läuft also alles gut. es gibt eine positive Antwort.
 
print(r.text)

from bs4 import BeautifulSoup 
soup = BeautifulSoup(r.text, 'html.parser') # aus meinem r.text wird ein navigierbares Objekt
 
print(soup.prettify()) # schönere Ausgabe des Soup-Objekts mit Einrückungen, nicht nötig, aber gut für den Test
print(soup.title )
 
soup.title.name # gibt mir den Namen des tags zurück. Der ist title. Danach haben wir ja gesucht.
 
soup.a # gibt mir den ersten Link komplett zurück, also mit allem HTML drumherum. Ginge auch mit p oder b, etc.
 
soup.a.attrs['href'] # gibt mir nur das Link-Ziel zurück. 'class' würde mir die Klassen zurückgeben.
 
soup.a.text # gibt mir nur den Text zurück, auf dem der Link liegt
 
soup.find_all('a') # findet alle Links und speichert sie als Liste. Über die kann ich drüber iterieren.
 
soup.find_all("div", class_="Klasse1 Klasse2gehtauch") # Sucht DIVs mit den angegebenen Klassennamen