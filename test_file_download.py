from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

def test_file_download():
    download_dir = os.path.abspath("downloads")

    os.makedirs(download_dir, exist_ok=True)

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_dir}
    options.add_experimental_option("prefs", prefs)


    driver = webdriver.Chrome(options=options)
    driver.get("https://the-internet.herokuapp.com/download")

    driver.find_element(By.LINK_TEXT, "some-file.txt").click()
    time.sleep(3)

    file_path = os.path.join(download_dir, "some-file.txt")
    assert os.path.exists(file_path)

    driver.quit()

