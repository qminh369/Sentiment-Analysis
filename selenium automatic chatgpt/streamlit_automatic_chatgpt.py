import openai
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--window-size=1920x1080")

driver = uc.Chrome(chrome_options=chrome_options)

# api key chatgpt
model = 'text-davinci-003'     
with open("B:\\Đồ án I\\Project I\\ChatGPT labelling\\apikey.txt","r") as f:
    openai.api_key = f.readline()

# Hàm để gọi đến OpenAPI / Phần ChatGPT
def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(
        engine= model,
        prompt = user_question,
        max_tokens = 128, 
        n = 1,      
        temperature = 0.5      
    )

    response_text = response.choices[0].text        
    return response_text

# Nhập prompt
with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\prompt.txt', 'r', encoding = 'utf-8') as file:
    prompt = file.read()
    
with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\comment.txt', 'r', encoding='utf-8') as file:
    comments = []
    for line in file:
        comments.append(line)

summarize = []
for i in range(0, len(comments)-5, 5):
    summarize.append(comments[i] + comments[i+1] + comments[i+2] + comments[i+3] + comments[i+4])

for i in range(3):
    response_text = get_response_from_chatgpt(prompt + summarize[i])
    st.write(f"{response_text}")
    time.sleep(20)

    # Mở trang web ChatGPT

    # driver.get('https://chat.openai.com/')
    driver.get('http://localhost:8501/')
    #driver.get('http://localhost:8502/')
    time.sleep(5)

    answer = driver.find_elements(By.XPATH, "//div[@class = 'element-container css-1hynsf2 e1tzin5v2']")[0]
    result = answer.text
    print(result)

    with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\result_api_selenium.txt', 'a', encoding = 'utf-8') as file:
        file.write(result + '\n')



time.sleep(5)
driver.quit()