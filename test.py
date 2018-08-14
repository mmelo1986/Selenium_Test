from selenium import webdriver
import time
import os
from time import sleep
#creating driver options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')

#creating chome driver
chromeDriver = webdriver.Chrome(chrome_options=options)
chromeDriver.get('https://www.ibindr.com/Login')

#storing username and password
uName = 'mmelo1986@gmail.com'
pWord = 'MMelo@1986'
#login in
chromeDriver.find_element_by_id('input_0').send_keys(uName)
chromeDriver.find_element_by_id('input_1').send_keys(pWord)
chromeDriver.find_element_by_xpath("//button[@type='submit']").click()
sleep(6)
#selecting sample project
chromeDriver.find_element_by_xpath('//*[@id="ui-swap-1"]/md-list-item[2]/div/button').click()
sleep(1)

chromeDriver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/button[2]/md-icon').click()
sleep(1)

files = os.listdir('C:/wamp/www/projects/includes/images')

for x in files:
    chromeDriver.find_element_by_xpath('//*[@id="fileUploadButton"]').send_keys('C:/wamp/www/projects/includes/images/'+x)
sleep(3)
chromeDriver.find_element_by_xpath('//*[@id="fileupload"]/div/div[1]/div[2]/button[1]').click()
sleep(2)
chromeDriver.find_element_by_xpath('/html/body/div[1]/div/md-list[2]/div[2]/div[2]/md-icon').click()
sleep(1)
chromeDriver.find_element_by_xpath('/html/body/div[1]/div/md-list[2]/div[1]/div[2]/img').click()
sleep(5)
chromeDriver.find_element_by_xpath('//*[@id="dialogContent_105"]/md-content/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[3]').click()
sleep(1)
chromeDriver.find_element_by_xpath('//*[@id="input-107"]').send_keys('Marco Melo')
sleep(1)
chromeDriver.find_element_by_xpath('//*[@id="ul-107"]/li[1]/md-autocomplete-parent-scope/span[2]').click()
sleep(1)
chromeDriver.find_element_by_xpath('//*[@id="fileInformation"]/div[2]/div[1]/div/div[1]/div[1]/md-icon').click()
sleep(1)
chromeDriver.find_element_by_xpath('/html/body/div[5]/md-dialog/md-toolbar/div/button/md-icon').click()

#chromeDriver.find_element_by_xpath('/html/body/div/md-sidenav/md-content/a[7]/div/div')
#chromeDriver.quit()
#files = os.listdir("./")
#print(files[1])