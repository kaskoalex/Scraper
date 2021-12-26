
1
2
3
import requests # Bibliothek wird importiert...
from bs4 import BeautifulSoup  
r = requests.get('http://www.benedict-witzenberger.de') # ... und kümmert sich von selbst um die Verbidung, auch https geht.
print(r.status_code)
#200 - läuft also alles gut. es gibt eine positive Antwort.
 
print(r.text)
# Zeigt mir die Antwort der Request an, in diesem Fall das HTML meines Blogs
# <!doctype html>
# <!--[if lt IE 7 ]> <html class="no-js ie6" lang="de-DE" prefix="og: http://ogp.me/ns#"> <![endif]-->
# <!--[if IE 7 ]>    <html class="no-js ie7" lang="de-DE" prefix="og: http://ogp.me/ns#"> <![endif]-->
# <!--[if IE 8 ]>    <html class="no-js ie8" lang="de-DE" prefix="og: http://ogp.me/ns#"> <![endif]-->
# <!--[if (gte IE 9)|!(IE)]><!--> <html class="no-js" lang="de-DE" prefix="og: http://ogp.me/ns#"> <!--<![endif]-->
# <head>
# 
# <meta charset="UTF-8" />
# <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
# <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
# usw....


from bs4 import BeautifulSoup3 # Die Bibliothek wird geladen, und zwar nur BeautifulSoup aus dem Paket bs4
soup = BeautifulSoup(r.text, 'html.parser') # aus meinem r.text wird ein navigierbares Objekt
 
print(soup.prettify()) # schönere Ausgabe des Soup-Objekts mit Einrückungen, nicht nötig, aber gut für den Test