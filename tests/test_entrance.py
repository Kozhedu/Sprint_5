from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators

name = 'Kodasf12'
email = 'Kozsdf@ya.ru'
password = '1234567'

#вход по кнопке «Войти в аккаунт» на главной
def test_entrance_account(driver):
    driver.find_element(*locators.Locators.but_get).click()
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


#вход через кнопку «Личный кабинет»
def test_entrance_button_personal(driver):
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

#вход через кнопку в форме регистрации
def test_entrance_registrayion_form(driver):
    driver.find_element(*locators.Locators.but_get).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.but_text_get))
    driver.find_element(*locators.Locators.but_reg).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.but_text_reg))
    driver.find_element(*locators.Locators.personal_gett).click()
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

#вход через кнопку в форме восстановления пароля
def test_entrance_password_form(driver):
    driver.find_element(*locators.Locators.button_personal).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.button_gett))
    #восстановить пароль
    driver.find_element(*locators.Locators.parol_pass).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.tezst_pass))
    driver.find_element(*locators.Locators.pass_pers).click()
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