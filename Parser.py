def scrap(html):
  from bs4 import BeautifulSoup
  import re

  def has_id(elem):
    return elem.has_attr('id')

  soup = BeautifulSoup(html, 'html.parser')
  mainDiv = soup.find(class_='l-sidebar__main')

  if mainDiv:
    isBundle = False
    paidBundles = []
    goldBundles = []
    for child in mainDiv.contents:
      if (child.name != None):
        if (child.name != 'div') :
          isBundle = False

        if isBundle:
          item = {}

          name = child.find(class_='bundle-card__name').contents[0].replace('-', '')
          item['Name'] = name
          
          price = child.find('div', class_='bundle-card__cost').contents[0][2:-1]
          goldCost = child.find(class_='gold-price__value')

          if price or goldCost:
            for info in ['Tokens', 'Credits']:
              node = child.find(string=re.compile(f".*{info}.*"))
              data = None
              if node:
                data = re.sub(pattern="[^\d]+", repl='', string=node)
              if data:
                item[info] = data
              else:
                item[info] = '0'
          
          if price:
            item['Cost'] = price
            paidBundles.append(item)
          if goldCost:
            item['Cost'] = goldCost.contents[0] + 'G'
            goldBundles.append(item)

        if (has_id(child) and re.match(pattern=".*Bundles.*", string=child.attrs['id']) != None and isBundle == False):
          isBundle = True

    return [paidBundles, goldBundles]
  else:
    print("The scrapped site structure probably changed, so the code is broken")
    return None
