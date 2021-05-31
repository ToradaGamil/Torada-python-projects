
from selenium import webdriver
from time import sleep

usr = input('Enter Email Id:')
pwd = input('Enter Password:')

driver = webdriver.Chrome("C:\Program Files/chromedriver.exe")
driver.get('https://www.facebook.com/')
print("Opened facebook")

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email Id entered")

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password entered")

login_box = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login_box.click()

print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")