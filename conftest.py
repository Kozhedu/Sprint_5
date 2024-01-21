import pytest
from selenium import webdriver

@pytest.fixture
# подключаем драйвер
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    
    driver.quit()