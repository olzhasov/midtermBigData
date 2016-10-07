from selenium import webdriver
import os
import xlwt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.bold = True
style0 = xlwt.XFStyle()
style0.font = font0
wb = xlwt.Workbook()
ws = wb.add_sheet('vesti', cell_overwrite_ok=True)
os.environ["webdriver.chrome.driver"] = "chromedriver"
driver = webdriver.Chrome("chromedriver")
driver.get("https://vesti.kz")
pos = 0
cnt = [cnt.text for cnt in driver.find_elements_by_xpath('//div[@class="single-item"]')]
links = [a.get_attribute('href') for a in driver.find_elements_by_xpath('//div[@class="single-item"]/a')]
title = []
ws.write(pos, 0, 'title', style0)
ws.write(pos, 1, 'comment', style0)

for i in range(len(cnt)):
    if cnt[i] != '0':   
        # print links[i]                                                                                                      
        driver.get(links[i])
        driver.implicitly_wait(10)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        while True:
            try:
                element = WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.ID, "jsBtn")))
                #element = driver.find_element_by_id("jsBtn")
                driver.execute_script("return arguments[0].scrollIntoView();", element)    
                element.click()
            except WebDriverException:
                break

        titles=driver.find_elements_by_xpath('.//h1[@class="inner-header"]')
        comments = driver.find_elements_by_class_name('comment-text')
        for i in titles:
            ws.write(pos+1, 0, i.text)
            for j in comments:
                ws.write(pos+1, 1, j.text)
                pos += 1

wb.save('midout.xls')








