# Проект автоматизации тестирования сервиса Stellar Burgers
1. Основа для написания автотестов — фреймворк pytest.
2. Команда для запуска — pytest -v. 

Все тесты → в директории tests:

test_registat.py сожержит два теста:
1. Успешную регистрацию. 
2. Ошибку для некорректного пароля.

test_entrance.py сожержит четыре теста: 
1. вход по кнопке «Войти в аккаунт» на главной странице
2. вход через кнопку «Личный кабинет»
3. вход через кнопку в форме регистрации
4. вход через кнопку в форме восстановления пароля

test_transition.py сожержит четыре теста:
1. Переход в личный кабинет
2. Переход из личного кабинета в конструктор 
3. Переход из личного кабинета через логотип
4. Выход

test_burger.py содержит три теста:
переходы к разделам:
«Булки»
«Соусы»
«Начинки».
