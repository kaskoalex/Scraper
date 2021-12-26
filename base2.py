
from bs4 import BeautifulSoup # Die Bibliothek wird geladen, und zwar nur BeautifulSoup aus dem Paket bs4
soup = BeautifulSoup(r.text, 'html.parser') # aus meinem r.text wird ein navigierbares Objekt
 
print(soup.prettify()) # schönere Ausgabe des Soup-Objekts mit Einrückungen, nicht nötig, aber gut für den Test



13
soup.title # gibt mir das erste Objekt zurück, das in Title-Tags steht. Gibt vermutlich nur eins auf der Seite
 
soup.title.name # gibt mir den Namen des tags zurück. Der ist title. Danach haben wir ja gesucht.
 
soup.a # gibt mir den ersten Link komplett zurück, also mit allem HTML drumherum. Ginge auch mit p oder b, etc.
 
soup.a.attrs['href'] # gibt mir nur das Link-Ziel zurück. 'class' würde mir die Klassen zurückgeben.
 
soup.a.text # gibt mir nur den Text zurück, auf dem der Link liegt
 
soup.find_all('a') # findet alle Links und speichert sie als Liste. Über die kann ich drüber iterieren.
 
soup.find_all("div", class_="Klasse1 Klasse2gehtauch") # Sucht DIVs mit den angegebenen Klassennamen