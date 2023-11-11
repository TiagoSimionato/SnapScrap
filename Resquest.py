def get(url = "https://snap.fan/news/schedule/"):
  from requests import get

  HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
  }

  return get(url, headers=HEADERS)
