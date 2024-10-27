from time import sleep
from bs4 import BeautifulSoup   
import requests
import pandas as pd
import re
import lxml 

headers={   
    
}
url = "https://xn--80aegj1b5e.xn--p1ai/factories?page=1"
page = requests.get("https://xn--80aegj1b5e.xn--p1ai/factories?page=1")
sleep(5)
print (page.text)
