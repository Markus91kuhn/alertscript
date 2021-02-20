from selenium import webdriver 

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

path = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(path+"/chromedriver") 
actionChains = ActionChains(driver)
driver.get(r'https://iapps.courts.state.ny.us/nyscef/DocumentList?docketId=npvulMdOYzFDYIAomW_PLUS_elw==&display=all')
pagenumbers=driver.find_element_by_class_name('pageNumbers')
lastpage=pagenumbers.find_elements_by_class_name('pageOff')
go_latest_page=lastpage[len(lastpage)-1]
go_latest_page.click()
result1=driver.find_element_by_class_name('NewSearchResults')
result2=result1.find_elements_by_tag_name('tr')
result3=result2[len(result2)-1].find_elements_by_tag_name('td')
result4=result3[2].text
result5=result4.split()
f = open("result.txt", "r")
checktext=f.read()
f.close()
if(checktext==result5):
    print('old')
else:
    f = open("result.txt", "w")
    f.write(result5)
    f.close()
    print('new')
# print(f.read())
# print(result5)

