
import requests  
r = requests.get(' http://www.example.com/') 
print(r.status_code)
#200 - läuft also alles gut. es gibt eine positive Antwort.
 
print(r.text)# !!!   HTML mit CSS und Text   !!!


from bs4 import BeautifulSoup # Die Bibliothek wird geladen, und zwar nur BeautifulSoup aus dem Paket bs4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/#porting-code-to-bs4
soup = BeautifulSoup(r.text, 'html.parser') # aus meinem r.text wird ein navigierbares Objekt

print(soup.prettify()) # schönere Ausgabe des Soup-Objekts mit Einrückungen, nicht nötig, aber gut für den Test

print(soup.title) #!!!   gibt  das Title zurück, das in Title-Tags steht     !!!!
 
print(soup.a) # gibt  den ersten Link komplett zurück, also mit allem HTML drumherum
#   !!!!  soud.   mit eingabe vot tag, gibt dem tag       !!!! 
print(soup.h1) # !!!!  soud.   mit eingabe vot tag, gibt dem tag       !!!! 

print(soup.a.attrs['href']) # gibt mir nur das Link-Ziel zurück. 'class' würde mir die Klassen zurückgeben.
 
print(soup.a.text) # gibt mir nur den Text zurück, auf dem der Link liegt
 
print(soup.find_all('a')) # findet alle Links und speichert sie als Liste. Über die kann ich drüber iterieren.

print(soup.find_all('p')) #!!!!    findet alle eingegebene tags , hier "p"  !!!

print(soup.find_all("div", class_="Klasse1 Klasse2gehtauch")) # Sucht DIVs mit den angegebenen Klassennamen

print(soup.contents)
print(len(soup.contents))
# 
print(soup.contents[0].name)
# 
print(len(list(soup.children)))
# 
print(len(list(soup.descendants)))
# 
import re
for tag in soup.find_all(re.compile("^m")):
    print(tag.name)
# !!!   findet alle tags mit eingegebene erste buchstabe  !!!
print(soup.find_all(["a", "p"]))
# !!!   findet alle tags mit eingegebene erste buchstabe  !!!

print(soup.find_all("p", "title"))
#find_all( name , attrs , recursive , string , limit , **kwargs )



print(soup.find_all(id=True))
#Dieser Code findet alle Tags, deren idAttribut einen Wert hat, unabhängig vom Wert:

print(soup.find_all("a", class_="sister"))
#  !!!!   Suche nach CSS-Klasse   !!!

soup.find_all("a", limit=2)
#Es weist Beautiful Soup an, das Sammeln von Ergebnissen einzustellen, nachdem eine bestimmte Zahl gefunden wurde.

print(soup.select("title"))
#Die SoupSieve- Dokumentation listet alle derzeit unterstützten CSS-Selektoren auf, aber hier sind einige der Grundlagen:

markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, 'html.parser')

print(soup.get_text())
'\nI linked to example.com\n'
print(soup.i.get_text())
'example.com'
#Wenn Sie nur den für Menschen lesbaren Text in einem Dokument oder Tag verwenden möchten,blindentext
