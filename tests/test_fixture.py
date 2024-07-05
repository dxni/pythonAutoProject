import csv
import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromerService
from webdriver_manager.chrome import ChromeDriverManager

#@pytest.fixture(params=["Playwright", "Selenium", "Cypress"])
#def termino_de_busqueda(request):
#    return request.param



@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com.bo/")
    yield driver
    driver.quit()
 
#Funcion especial para leer el csv
def read_search_terms():
    with open('TestData/busquedaGoogle.csv', newline= '') as csvfile:  
        data = list(csv.reader(csvfile))
        #Devuelve los terminos de busqueda excepto el titulo de la columna
    return[row[0] for row in data [1:]]
    
    
#fixture para parametrizar los terminos de busqueda desde el csv
@pytest.fixture(params=read_search_terms())
def termino_de_busqueda (request):
    return request.param

#test que utiliza los datos que viene del CSV   
def test_google_busqueda(browser,termino_de_busqueda): ##Busca los parametros de arriba en la pagina de google
    campo_de_busqueda=browser.find_element("name","q")
    campo_de_busqueda.send_keys(termino_de_busqueda + Keys.RETURN)
    
    results= browser.find_element("id","search")
    assert (len(results.find_elements("xpath", ".//div"))>0), "Hay resultados de busqueda"
    