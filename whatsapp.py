from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver=webdriver.Chrome()

baseurl="https://web.whatsapp.com"

driver.get(baseurl)

time.sleep(30)
with open("contact.csv",newline='')as csvfile:
    readcontacts=csv.reader(csvfile)
    for phone,msg in readcontacts:
        phonenum=phone
        message=msg

        sameTab=(baseurl+"/send?phone="+str(phonenum))

        driver.get(sameTab)

        time.sleep(10)

        content=driver.switch_to.active_element

        content.send_keys(message)


        content.send_keys(Keys.RETURN)
        time.sleep(10)