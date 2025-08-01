from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/droppable/")
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)

drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")

ActionChains(driver).drag_and_drop(drag, drop).perform()

sleep(30)
driver.quit()