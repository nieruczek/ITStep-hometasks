from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import random

path = os.path.join("", "text1.txt")                            # створюю або чищу файл, куди записую отриману інформацію
myfile = open(path, 'w')
myfile.write("")
myfile.close()

hrefs = []                                                      # список для посилань на сторінки героїв

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\ItStep_Lessons\\Python\\selenium_python\\dz4\\chromedriver.exe")
wait = WebDriverWait(agent_ghost, 10)

def append_to_hrefs():                                                                      # функція для отримання посилань на сторінки героїв
    try:
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'explore__link')))
        step1 = agent_ghost.find_elements(By.CLASS_NAME, 'explore__link')
        for element in step1:
            step2 = element.get_attribute('href')
            hrefs.append(step2)
        return hrefs
    except:
        pass

agent_ghost.get(url="https://www.marvel.com/")
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/header/nav/div/section[2]/div/div[2]/ul/li[3]/a")))
button1 = agent_ghost.find_element(By.XPATH, "/html/body/div[1]/div/div/header/nav/div/section[2]/div/div[2]/ul/li[3]/a")
button1.click()

# Кнопка Next для гортання сторінок мені не підкорилася, бо її селектори трохи міняються в залежності від нумерації
# Тому я прописала окремо варіанти всіх можливих положень кнопок для переходу на наступну сторінку
# Більшість йде через цикл for

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[1]/span')))  #1
button2 = agent_ghost.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[1]/span')
button2.click()
append_to_hrefs()

# тут зчитується загальна кількість сторінок, щоб пройти їх всі
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[7]/span')))
step4 = agent_ghost.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[7]/span').get_attribute('aria-label')
step5 = list(step4)
step7 = []
for step6 in step5:
    if step6.isdigit():
        step7.append(step6)
step8 = "".join(step7)
step9 = int(step8)

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[2]/span'))) #2
button3 = agent_ghost.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[2]/span').click()
append_to_hrefs()


wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[4]/span'))) #3
button4 = agent_ghost.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[4]/span').click()
append_to_hrefs()


wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[5]/span')))  # 4
button5 = agent_ghost.find_element(By.XPATH,'/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[5]/span').click()
append_to_hrefs()

for x in range(step9 - 6):
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[6]/span')))  # 5
    button6 = agent_ghost.find_element(By.XPATH,'/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[6]/span').click()
    append_to_hrefs()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[7]/span')))  # 75
button8 = agent_ghost.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[7]/span').click()
append_to_hrefs()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[8]/span')))  # 76
button9 = agent_ghost.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[8]/span').click()
append_to_hrefs()

myfile = open(path, 'a')                    #відкриваю файл для запису даних

myhref = list(set(hrefs))                   #забираю зі списку посилань на сторінки персонажів елементи, що повторюються

for e in random.sample(myhref, 10):         #обираю з отриманого списку 10 рандомних персонажів а зачитую дані
    step10 = agent_ghost.get(f'{e}')
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#masthead-1 > div > div > div.masthead__hero > div > div > h1 > span.masthead__headline' )))
        step11 = agent_ghost.find_element(By.CSS_SELECTOR, '#masthead-1 > div > div > div.masthead__hero > div > div > h1 > span.masthead__headline')
        myfile.write(step11.text + "\n")
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#two_column-4 > div > div.flex-col-fixed.two-column__rail > div.railExploreBio > div.collapsible > div.accordion-collapse.open')))
            step12 = agent_ghost.find_element(By.CSS_SELECTOR, '#two_column-4 > div > div.flex-col-fixed.two-column__rail > div.railExploreBio > div.collapsible > div.accordion-collapse.open')
            myfile.write(step12.text + "\n")
            myfile.write("\n")
        except:
            myfile.write("Information about character not found\n")

    except:
        myfile.write("No superhero\n")
        myfile.write("\n")

myfile.close()
agent_ghost.close()
