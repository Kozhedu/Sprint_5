from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
#переход на  соусы
def test_sauces (driver):
     driver.find_element(*locators.Locators.sauces).click()
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.sauces_txt))
     assert driver.find_element(*locators.Locators.sauces_txt).text == 'Соусы'

#переход на начинки
def test_filling (driver):
    driver.find_element(*locators.Locators.filling).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.filling_txt))
    assert driver.find_element(*locators.Locators.filling_txt).text == 'Начинки'

#переход на булки
def test_rolls (driver):
    driver.find_element(*locators.Locators.sauces).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.sauces_txt))
    driver.find_element(*locators.Locators.rolls).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.rolls_txt))
    assert driver.find_element(*locators.Locators.rolls_txt).text == 'Булки'