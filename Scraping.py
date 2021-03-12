import selenium
    
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


import requests
from bs4 import BeautifulSoup
import pandas as pd
from random import randrange
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import smtplib, ssl
from sqlalchemy import create_engine
driver = webdriver.Chrome(ChromeDriverManager().install())
def toExcel(df, name):
    writer = pd.ExcelWriter(name+'.xlsx')
    df.to_excel(writer,'Sheet1')
