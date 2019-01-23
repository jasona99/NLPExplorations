#Jason Ashley
import nltk
import urllib.request
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#print(x.translate(non_bmp_map))
url = input("URL: ")
response = urllib.request.urlopen(url)
html = response.read()
print(html)
soup = BeautifulSoup(html,features="html.parser")
text = soup.get_text(strip = True)
#print(text)
tokens = [t for t in text.split()]
#print(tokens)
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
#for key, val in freq.items():
    #print(str(key) + ':' + str(val))

freq.plot(20, cumulative = False)
