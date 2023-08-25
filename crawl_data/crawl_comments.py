from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

chrome_driver_path = 'B:\\Q.Minh Hust\\Project\\TIki Sentiment Analysis\\chromedriver.exe'
chrome_service = Service(chrome_driver_path, options = chrome_options)
driver = webdriver.Chrome(service=chrome_service)

links_data = pd.read_csv('B:\\Đồ án I\\Project I\\crawl_data\\links.csv', header=None)
links = links_data[0]
# print(links)

for link in links[11:15]:
    driver.get(link)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    time.sleep(2)
    
    elements = driver.find_elements(By.XPATH, "//div[@class='review-comment__content']")
    comments = [el.text for el in elements]

print(comments)

