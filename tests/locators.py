from selenium.webdriver.common.by import By
class Locators:
    but_get = By.XPATH, '//button[text()="Войти в аккаунт"]' # кнопка "Войти в аккаунт"
    but_text_get = By.XPATH, '//*[text()="Вход"]' # текст "Вход"
    but_reg = By.CLASS_NAME, 'Auth_link__1fOlj'#кнопка "Зарегистрироваться"
    but_text_reg = By.XPATH, '//*[text()="Регистрация"]'  # текст "Регистрация"
    input_1 = By.XPATH, './/fieldset[1]//input' #поле для ввода 1
    input_2 = By.XPATH, './/fieldset[2]//input' #поле для ввода 2
    input_3 = By.XPATH, './/fieldset[3]//input' #поле для ввода 3
    button_reg = By.XPATH, '//button[text()="Зарегистрироваться"]' #кнопка "Зарегистрироваться"
    entrance_text = By.XPATH, '//*[text()="Вход"]' # текст "Вход"
    incorrect = By.XPATH, '//p[contains(text(),"Некорректный пароль")]' #текст "Некорректный пароль"
    account_txt = By.XPATH, '//button[text()="Войти в аккаунт"]' #текст "Войти в аккаунт"
    button_gett = By.XPATH, '//button[text()="Войти"]' #кнопка войти
    button_lt = By.XPATH, '//*[text()="Личный Кабинет"]' #кнопка Личный кабинет
    txt_lt = By.XPATH, '//*[text()="В этом разделе вы можете изменить свои персональные данные"]'
    text_name_in = By.XPATH, '//li[1]//input' #Поле с имененм
    email_text = By.XPATH, '//input[@type="text"]' #Поле для ввода email
    passvord_text = By.XPATH, '//input[@type="password"]' #Поле для ввода password
    button_personal = By.XPATH, '//*[text()="Личный Кабинет"]' #текст личный кабинет
    personal_gett = By.XPATH, "//a[contains(text(),'Войти')]" # Вотйи
    parol_pass = By.XPATH, '//a[text()="Восстановить пароль"]' #Восстановить пароль
    tezst_pass = By.XPATH, '//*[text()="Восстановление пароля"]' #Восстановление пароля
    pass_pers = By.XPATH, '//a[text()="Войти"]' #Войти
    but_cons = By.XPATH, './/p[text()="Конструктор"]' #Конструктор
    bur_test = By.XPATH, ".//h1[text()='Соберите бургер']" #Соберите бургер
    logo_get = By.XPATH, '//nav/div[@class="AppHeader_header__logo__2D0X2"]' #логитип
    get_logo = By.XPATH, '//button[text()="Выход"]' #кнопка Вход
    sauces = By.XPATH, '//span[contains(text(), "Соусы")]' #Кнопка соусы
    sauces_txt = By.XPATH, '//h2[contains(text(), "Соусы")]' #текст соусы

    filling = By.XPATH, '//span[contains(text(), "Начинки")]' #Кнопка начинки
    filling_txt = By.XPATH, '//h2[contains(text(), "Начинки")]' #текст начинки

    rolls = By.XPATH, '//span[contains(text(), "Булки")]' #Кнопка булки
    rolls_txt = By.XPATH, '//h2[contains(text(), "Булки")]' #текст булки