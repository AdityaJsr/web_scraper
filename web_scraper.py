from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions
option.add_argument('--incognito')

browser = webdriver.Chrome(executable_path="C:\chrome driver\chromedriver_win32\chromedriver.exe", chrome_options= option)

browser.get('https://www.amazon.in/s?k=1660+super&crid=GJCRBFWHHE4R&sprefix=1660+s%2Caps%2C477&ref=nb_sb_ss_i_1_6')

timeout = 10

try:
    WebDriverWait(browser, timeout).until(ES.visibility_of_element_located((By.XPATH,"//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[10]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")))
    