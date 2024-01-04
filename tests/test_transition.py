from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators

email = 'Kozsdf@ya.ru'
password = '1234567'
name = 'Kodasf12'

url = 'https://stellarburgers.nomoreparties.site/'
url_exit = 'https://stellarburgers.nomoreparties.site/login'

#Переход в личный кабинет
def test_personal(driver):
    driver.find_element(*locators.Locators.button_personal).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_gett))
    #Ввод данных
    driver.find_element(*locators.Locators.email_text).send_keys(email)
    driver.find_element(*locators.Locators.passvord_text).send_keys(password)
    driver.find_element(*locators.Locators.button_gett).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_lt))
    #Переход в личный кабинет
    driver.find_element(*locators.Locators.button_lt).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.txt_lt))
    #Проверка
    assert driver.find_element(*locators.Locators.text_name_in).get_attribute('value') == name
#Переход из личного кабинета в конструктор 
def test_cons(driver):
    driver.find_element(*locators.Locators.button_personal).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_gett))
    #Ввод данных
    driver.find_element(*locators.Locators.email_text).send_keys(email)
    driver.find_element(*locators.Locators.passvord_text).send_keys(password)
    driver.find_element(*locators.Locators.button_gett).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_lt))
    #Переход в личный кабинет
    driver.find_element(*locators.Locators.button_lt).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.txt_lt)) 
    #Переход через конструктор
    driver.find_element(*locators.Locators.but_cons).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.bur_test)) 
    assert driver.current_url == url
##Переход из личного кабинета через логотип
def test_cons_logo(driver):
    driver.find_element(*locators.Locators.button_personal).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_gett))
    #Ввод данных
    driver.find_element(*locators.Locators.email_text).send_keys(email)
    driver.find_element(*locators.Locators.passvord_text).send_keys(password)
    driver.find_element(*locators.Locators.button_gett).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_lt))
    #Переход в личный кабинет
    driver.find_element(*locators.Locators.button_lt).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.txt_lt)) 
    #Переход через логотип
    driver.find_element(*locators.Locators.logo_get).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.bur_test)) 
    assert driver.current_url == url

#выход
def test_cons_exit(driver):
    driver.find_element(*locators.Locators.button_personal).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_gett))
    #Ввод данных
    driver.find_element(*locators.Locators.email_text).send_keys(email)
    driver.find_element(*locators.Locators.passvord_text).send_keys(password)
    driver.find_element(*locators.Locators.button_gett).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_lt))
    #Переход в личный кабинет
    driver.find_element(*locators.Locators.button_lt).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.txt_lt)) 
    #выход
    driver.find_element(*locators.Locators.get_logo).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.but_text_get))
    assert driver.current_url == url_exit
