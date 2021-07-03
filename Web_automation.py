#WEB_AUTOMATION

from selenium import webdriver   #importing selenium

browser = webdriver.Chrome(executable_path = "D:\\chromedriver_win32\\chromedriver.exe")
browser.get("https://codechef.com")
user_name = browser.find_element_by_id("edit-name")
user_name.send_keys("pkcalm_2206")
user_password = browser.find_element_by_id("edit-pass")
from getpass import getpass 
user_password.send_keys(getpass("Enter the password:"))
browser.find_element_by_id("edit-submit").click()
browser.get("https://www.codechef.com/submit/TEST")
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

with open("Web_automation.py", 'r') as f:
    code = f.read()

code_element = browser.find_element_by_id("edit-program")

code_element.send_keys(code)
browser.find_element_by_xpath('//*[@id="edit.language"]/option[2]').click()       #Language_Select
browser.find_element_by_id("edit-submit").click()                                 #Final_Submission

#finished