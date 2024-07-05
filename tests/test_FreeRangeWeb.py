import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@pytest.mark.cursos
def test_navegacion_free_range_page_web():
    driver.get("https://www.freerangetesters.com/")
    driver.find_element(By.XPATH, "//a[normalize-space()='Cursos' and @href]").click()
    

    
    