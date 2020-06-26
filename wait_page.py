from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


  # si antes de los 50 se carga entra
  wait = WebDriverWait(driver, 50) 
    export = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='export_button']")))
    ActionChains(driver).move_to_element(export).perform()
    driver.find_element_by_xpath("//*[@id='export_button']").click()
