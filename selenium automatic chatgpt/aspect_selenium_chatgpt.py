from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time

chrome_options = Options()
driver = uc.Chrome(chrome_options=chrome_options)

# Nhập prompt
with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\prompt_aspect.txt', 'r', encoding = 'utf-8') as file:
    prompt = file.read()
    
with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\comment.txt', 'r', encoding='utf-8') as file:
    comments = []
    for line in file:
        comments.append(line)

summarize = []
for i in range(0, len(comments)-5, 5):
    summarize.append(comments[i] + comments[i+1] + comments[i+2] + comments[i+3] + comments[i+4])

# Mở trang web ChatGPT
driver.get('https://chat.openai.com/auth/login')
time.sleep(1)

# Đăng nhập tài khoản chatgpt
button_login = driver.find_element(By.XPATH, "//button[@class='btn relative btn-primary'][1]")
button_login.click()
time.sleep(3)

account = 'quangminhpulisic123@gmail.com'
password = 'minhboy123'

#account = 'tungteng0401@gmail.com'    
#password = '@jTtM*wUvT4B62.'

#account = 'phanan1227@gmail.com'
#password = 'phanlacan12'

#account = 'sktblank2212@gmail.com'
#password = 'minhkepa2212'

#account = 'niallerjamespotter@gmail.com'
#password = '12345678'

# Nhập tài khoản, mật khẩu
mail = driver.find_elements(By.TAG_NAME, "input")[1]
mail.send_keys(account)
btn = driver.find_elements(By.TAG_NAME,"button")[0]
btn.click()

pw = driver.find_elements(By.TAG_NAME,"input")[2]
pw.send_keys(password)

btn = driver.find_element(By.XPATH, "//button[@class = 'c3768468a cd7c8bf9c c4a5884bf c127814b1 _button-login-password']")
btn.click()
time.sleep(2)

btn1 = driver.find_element(By.XPATH, "//button[@class = 'btn relative btn-neutral ml-auto']")
btn1.click()
time.sleep(2)
btn2 = driver.find_element(By.XPATH, "//button[@class = 'btn relative btn-neutral ml-auto']")
btn2.click()
time.sleep(2)
btn3 = driver.find_element(By.XPATH, "//button[@class = 'btn relative btn-primary ml-auto']")
btn3.click()
time.sleep(2)

for i in range(3):
    text_area = driver.find_element(By.TAG_NAME, "textarea")
    driver.execute_script("arguments[0].value = arguments[1];", text_area, prompt + summarize[i])
    text_area.send_keys(Keys.ENTER)

    btn_answer = driver.find_element(By.XPATH, "//button[@class = 'absolute p-1 rounded-md md:bottom-3 md:p-2 md:right-3 dark:hover:bg-gray-900 dark:disabled:hover:bg-transparent right-2 disabled:text-gray-400 enabled:bg-brand-purple text-white bottom-1.5 transition-colors disabled:opacity-40']")
    btn_answer.click()
    time.sleep(30)
    
    answer = driver.find_elements(By.XPATH, "//div[@class = 'markdown prose w-full break-words dark:prose-invert light']")[i]
    result = answer.text
    print(result)

    with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\result_aspect.txt', 'a', encoding = 'utf-8') as file:
        file.write(result + '\n')

    time.sleep(5)

driver.quit()