from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/buttons")
double_click_button = driver.find_element(By.ID, "doubleClickBtn")
ActionChains(driver).double_click(double_click_button).perform()

message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "doubleClickMessage"))
)

assert "You have done a double click" in message.text

sleep(2)
driver.quit()