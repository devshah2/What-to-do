from selenium import webdriver
from selenium.webdriver.common.by import By

netId=input("Netid: ")
pwd=input("Password: ")

driver = webdriver.Chrome('./chromedriver')

# Login
driver.get("https://caesar.ent.northwestern.edu/")

netIdField = driver.find_element(By.ID,"idToken1")
pwdField = driver.find_element(By.ID,"idToken2")

netIdField.clear()
netIdField.send_keys(netId)

pwdField.clear()
pwdField.send_keys(pwd)

driver.find_element(By.ID,"loginButton_0").click()

while True:

    pass