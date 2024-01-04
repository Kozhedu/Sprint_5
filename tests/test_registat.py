from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators

url = 'https://stellarburgers.nomoreparties.site/'

#Корректная регистрация
def test_registration(driver):
    name = 'Lns19842222'
    email = 'Lns19842222@ya.ru'
    password = '1234567'
    #Войти в аккаунт
    driver.find_element(*locators.Locators.but_get).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((locators.Locators.but_text_get)))
    #Зарегистрироваться
    driver.find_element(*locators.Locators.but_reg).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.but_text_reg))
    #Ввод данных
    driver.find_element(*locators.Locators.input_1).send_keys(name)
    driver.find_element(*locators.Locators.input_2).send_keys(email)
    driver.find_element(*locators.Locators.input_3).send_keys(password)

    driver.find_element(*locators.Locators.button_reg).click()
    #Проверка
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.entrance_text))
    assert driver.current_url == url + 'login'

#Ошибка для некорректного пароля.
def test_not_password(driver):
    name2 = 'Lns1984222212'
    email2 = 'Lns19842222112@ya.ru'
    password2 = '123'
    #Войти в аккаунт
    driver.find_element(*locators.Locators.but_get).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.but_text_get))
    #Зарегистрироваться
    driver.find_element(*locators.Locators.but_reg).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.but_text_reg))
    #Ввод данных
    driver.find_element(*locators.Locators.input_1).send_keys(name2)
    driver.find_element(*locators.Locators.input_2).send_keys(email2)
    driver.find_element(*locators.Locators.input_3).send_keys(password2)

    driver.find_element(*locators.Locators.button_reg).click()
    #Проверка
    assert driver.find_element(*locators.Locators.incorrect).text == "Некорректный пароль"