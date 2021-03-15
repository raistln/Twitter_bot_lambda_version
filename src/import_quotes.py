import logging
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

def import_quotes():
    logger.info("find a page to scrap some quotes")
    results = requests.get("https://parade.com/1079501/stephanieosmanski/sarcastic-quotes/")
    print(results)
    soup = BeautifulSoup(results.content,"html.parser")
    strongs = soup.find_all("p")
    quotes_lst = []
    final_quotes = []
    for strong in strongs:
        quote = strong.text
        quotes = quote.replace("\n","")
        try:
            if len(quotes)>2 and isinstance(int(quotes[0]),int):
                string = quote.encode('ascii', 'replace')
                quotes_lst.append(string)
        except: continue
    logger.info("try to do it a little better")
    for i in quotes_lst:
        a = i.decode("ascii").split(r"\?\?")
        a = re.split(r"\?\?|\.\?| \?", a[0])
        if len(a[1]) > 5:
            a = a[1]
        else:
            a = a[2]
        if a[0] == "?":
            a = a[1:]
        b = a[:-2].replace("?","´") + a[-2:]
        final_quotes.append(b)
    df = pd.DataFrame(final_quotes)
    df.to_csv("stewie_angry.csv", index=False)
