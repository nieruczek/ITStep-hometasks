from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path

path = os.path.join("", "text1.txt")


agent_007 = webdriver.Chrome(executable_path="D:\\GALYA\\PythonProjects\\pythonProject\\chromedriver.exe")

agent_007.get(url="https://www.ukr.net/")

wiki = agent_007.find_elements(By.CLASS_NAME, "feed__item--title")
my_file = open(path, "w")

for i in wiki:
    my_file.write(i.text + "\n")

agent_007.close()

my_file.close()
