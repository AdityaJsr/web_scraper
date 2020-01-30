from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path="C:\chrome driver\chromedriver_win32\chromedriver.exe", chrome_options= option)

browser.get('https://www.amazon.in/s?k=1660+super&crid=GJCRBFWHHE4R&sprefix=1660+s%2Caps%2C477&ref=nb_sb_ss_i_1_6')

timeout = 10

try:
    WebDriverWait(browser, timeout).until(ES.visibility_of_element_located((By.XPATH,('//*[@id="p_72/1318476031"]/span/a/section/i'))))
except TimeoutException:
    print("Oops Error Timeout")
    browser.quit()

title_element = browser.find_elements_by_xpath('//*[@id="search"]/div/div/div/span/div/div/div/span/div/div/div/div/div/div/div/div/div/h2/a/span')
title = [x.text for x in title_element]

'''it can also be written as
title = []
for x in title_elements:
    title.append(x.text)'''

print(title)


value_element = browser.find_elements_by_xpath('//*[@id="search"]/div/div/div/span/div/div/div/span/div/div/div/div/div/div/div/div/div/div/div/a/span/span/span')
value = [x.text for x in value_element]
#The website was returning 2 different values of a single GPU and every alternative value was true hence line 36 fixed that issue.
Price = [value[i] for i in range(len(value)) if i % 2 != 0] 
print(Price)
# print(len(value))

for title,Price in zip(title, Price):
    print(title +' :' + Price)
