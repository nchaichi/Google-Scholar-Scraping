from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd
import time
from datetime import datetime
from collections import OrderedDict
import re

scraped_data = []

chrome_path = "chromedriver.exe directory path"
browser = webdriver.Chrome(chrome_path)

with open("D:\article.csv", 'rb') as f:
    reader = csv.reader(f)
    for row in reader:

        row_dict = OrderedDict()
        row_dict["Article"] = row

        browser.get('https://scholar.google.com/')
        inputElement = browser.find_element_by_xpath("""//*[(@id = "gs_hp_tsi")]""")
        time.sleep(2)
        inputElement.send_keys(row)

        time.sleep(3)
        browser.find_element_by_xpath("""//*[(@id = "gs_hp_tsb")]""").click()

        time.sleep(30)
        browser.find_element_by_link_text("Cite").click()


        time.sleep(3)
        row_dict["Citation"] = browser.find_element_by_xpath("""//*[@id="gs_top"]""").find_element_by_xpath(
                """//*[@id="gs_md_w"]""").find_element_by_class_name("gs_citr").text


        scraped_data.append(row_dict)
        time.sleep(30)

df = pd.DataFrame(scraped_data)
df.to_csv('citation.csv', encoding = 'utf-8')