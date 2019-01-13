import requests

def crawl(url):
    result = requests.get(url)
    return result.content

