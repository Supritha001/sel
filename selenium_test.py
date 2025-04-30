import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_selenium():
    # Automatically download and use the latest chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("22CE1211 Supritha Yogesh Anchan")
    search_box.submit()
    
    if 'JENKINS_HOME' not in os.environ:
        input("Press enter to close the browser...")
    else:
        time.sleep(10)
    
    driver.quit()

test_selenium()
