from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def pesquisa():
    driver.find_element(By.XPATH, value="/html/body/div[1]/div/ul[1]/li[2]/a").click()
    driver.find_element(By.XPATH, value="/html/body/div[2]/div[1]/div[2]/ul/li[2]/a/div[2]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/ul/li[2]/ul/li[3]/a").click()
    time.sleep(10)
    driver.find_element(By.ID, value="post-search-input").send_keys("Nome na pesquisa")
    driver.find_element(By.ID, value="search-submit").click()

def acessando(lista_Nomes):
    driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form[1]/table/tbody/tr/td[1]/strong/a").click()
    time.sleep(20)
    driver.find_element(By.XPATH, value="//*[@id='tab-learndash_course_builder']").click()
    driver.find_element(By.XPATH, value="//*[@id='learndash_builder_box_wrap']/div/main/div/div[2]/div[1]/button").click()
    time.sleep(10)

    for licoes in lista_Nomes:
        driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/form/div/div/div/div[3]/div[2]/div/div/main/div/div[2]/div[1]/div/form/input").send_keys(licoes) 
        driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/form/div/div/div/div[3]/div[2]/div/div/main/div/div[2]/div[1]/div/form/span/input[1]").click()
        time.sleep(10)
        driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/form/div/div/div/div[3]/div[2]/div/div/main/div/div[2]/div[1]/button").click()
        time.sleep(10)


driver = webdriver.Firefox()

driver.get("Link do site")
#parada para sinalizar que efetuou o login no site
x = input("já realizou o login? ")
#lista_Nomes onde vai conter um seguencia de Strings para a criação de conteudo
lista_Nomes = [""]


pesquisa()
time.sleep(15)
acessando(lista_Nomes)