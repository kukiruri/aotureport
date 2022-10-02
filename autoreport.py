import time
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




def getDriver():
    if getattr(sys, 'frozen', False):
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        driver = webdriver.Chrome(chromedriver_path)
    else:
        driver = webdriver.Chrome(executable_path='本地chromedriver的路径') 
    return  driver


import os
os.getcwd()
root = os.getcwd()
data_dir = root 
print(root)


file_dir = root
file_name = 'username.txt'
f1 = open(file_name) .readline()

print(f1)

if __name__ == '__main__':
    input_path = "username.txt"
    var = None
    with open(input_path, "r") as fin:
        n_lines = 0
        for line in fin:
            n_lines += 1
            if 2 == n_lines:
                var = line.strip()
                break
    print(var)



web = Chrome()
web.set_window_size(500, 1000)
time.sleep(2.5)
web.get("https://hf.gzzhyc.cn/")
time.sleep(1)

username = f1
password = var
elusername = web.find_element(By.XPATH,r'//*[@id="app"]/form/div[1]/div[2]/div[1]/input')
elusername.click()
time.sleep(1)
elusername.send_keys(username) 
elpassword = web.find_element(By.XPATH,r'//*[@id="app"]/form/div[2]/div[2]/div[1]/input')    
elpassword.click()    
elpassword.send_keys(password, Keys.ENTER)  
time.sleep(3.5) 
web.get("https://hf.gzzhyc.cn/student/StuHealthForm") 
time.sleep(3.5) 
el3 = web.find_element(By.XPATH,r'/html/body/div[3]/div[3]/button')
el3.click()
time.sleep(1)
el5 = web.find_element(By.XPATH,r'//*[@id="app"]/div[1]/form/div[8]/div/i')
el5.click()
time.sleep(2)
el7 = web.find_element(By.XPATH,r'//*[@id="app"]/div[3]/div/div[1]/button[2]') 
el7.click() 
time.sleep(2)
el9 = web.find_element(By.XPATH,r'//*[@id="app"]/div[1]/form/div[10]/div/i') 
el9.click() 
time.sleep(2)
el11 = web.find_element(By.XPATH,r'//*[@id="app"]/div[5]/div/div[1]/button[2]')
el11.click() 
time.sleep(2)
el13 = web.find_element(By.XPATH,r'//*[@id="app"]/div[1]/form/div[16]/div/i')
el13.click() 
time.sleep(2)
el15 = web.find_element(By.XPATH,r'//*[@id="app"]/div[7]/div/div[1]/button[2]')
el15.click() 
time.sleep(2)
el17 = web.find_element(By.XPATH,r'//*[@id="app"]/div[1]/form/div[19]/div[1]/i')
el17.click() 
time.sleep(2)
el19 = web.find_element(By.XPATH,r'//*[@id="app"]/div[1]/form/div[19]/div[2]/div[2]/div/div[1]/button[2]')
el19.click() 
time.sleep(2)
el21 = web.find_element(By.XPATH,r'//*[@id="app"]/div[1]/form/div[23]/button[2]')
el21.click() 
time.sleep(2)

web.close()