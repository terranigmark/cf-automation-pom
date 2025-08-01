from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/menu")
menu_item_2 = driver.find_element(By.XPATH, "//ul[@id='nav']/li[2]")

ActionChains(driver).move_to_element(menu_item_2).perform()

submenu = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']"))
)

sleep(10)
driver.quit()
