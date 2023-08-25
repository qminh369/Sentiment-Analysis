from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv 
import numpy as np

# set up chrome driver
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

chrome_driver_path = 'B:\\Q.Minh Hust\\Project\\TIki Sentiment Analysis\\chromedriver.exe'
chrome_service = Service(chrome_driver_path, options = chrome_options)
driver = webdriver.Chrome(service=chrome_service)

# Crawl link
url= "https://tiki.vn/nha-sach-tiki/c8322?src=c.8322.hamburger_menu_fly_out_banner&page="

links = []
for i in range(1, 50):
    driver.get(url + str(i))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    elem = driver.find_elements(By.XPATH, "//a[@class='product-item']")
    
    lt = []
    lt = [el for el in elem]
    for l in lt:
        links.append(l.get_attribute('href'))
        
# save data to csv
filename = 'B:\\Đồ án I\\Project I\\crawl_data\\links.csv'
l = np.array(links)
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in range(0, l.shape[0]):
        myList = []
        myList.append(l[row])
        writer.writerow(myList)



