from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'Enter you username here'
passwordStr = 'Enter your password here'

browser = webdriver.Chrome()
browser.get(('https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2F'))

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

nextButton = browser.find_element_by_id('login')
nextButton.click()