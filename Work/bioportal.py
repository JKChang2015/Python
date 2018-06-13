# bioportal
# Created by JKChang
# 12/06/2018, 10:03
# Tag:
# Description: 

import urllib.request


from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# url = 'https://bioportal.bioontology.org/ontologies'
driver = webdriver.PhantomJS()
driver.get("https://bioportal.bioontology.org/ontologies")

wait = WebDriverWait(driver, 10)

# click proceed
proceed = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed")))
proceed.click()

# wait for the content to be present
wait.until(EC.presence_of_element_located((By.ID, "workskin")))

soup = BeautifulSoup(driver.page_source, "html.parser")
soup.prettify()