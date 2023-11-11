from bs4 import BeautifulSoup
import re

def has_id(elem):
  return elem.has_attr('id')

def h3class(elem):
  return elem

with open("./test.html", 'r') as file:
  html = file.read()

soup = BeautifulSoup(html, 'html.parser')
mainDiv = soup.find(class_='l-sidebar__main')
a = mainDiv.find_all(["h3", "div"], class_="my-3")
b = mainDiv.findAll('h3', id=re.compile(".*Bundles.*"))

isBundle = False
paidBundles = []
goldBundles = []
for child in mainDiv.contents:
  if (child.name != None):
    if (child.name != 'div') :
      isBundle = False

    if (isBundle):
      price = child.find('div', class_='bundle-card__cost').contents[0][2:-1]
      if price:
        node = child.find(string=re.compile(".*Tokens.*"))
        print(node)
        if node:
          tokens = re.search(pattern="[\n]*", string=node.get_text)
        else:
          tokens = "0"
        item = {
          "tokens"  : tokens
        }
        paidBundles.append(item)
      
      goldCost = child.find(class_='gold-price__value')
      if (goldCost):
        pass
        #print(goldCost.get_text())

    if (has_id(child) and re.match(pattern=".*Bundles.*", string=child.attrs['id']) != None and isBundle == False):
      isBundle = True
  #print(elment.find_all("h3", id))

print(paidBundles)