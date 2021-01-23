import requests
import re
from bs4 import BeautifulSoup
from bs4 import *

def getInformation(r):
    bs=BeautifulSoup(r,'html.parser')


