from time import sleep
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/dynamic-properties")

driver.find_element(By.ID, "enableAfter").click()

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[StaleElementReferenceException]
)

message = wait.until(
    EC.visibility_of_element_located((By.ID, "visibleAfter"))
)

sleep(3)
driver.quit()