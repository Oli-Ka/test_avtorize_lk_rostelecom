import os
from pages.base_page import WebPage
from pages.elements import WebElement

class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        web_driver.maximize_window()
        url = os.getenv("LOGIN_URL") or 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)


    # СТРАНИЦА АВТОРИЗАЦИИ ////////////////////////////////////////////////

    # Кнопка Зарегистрироваться
    link_register = WebElement(id="kc-register")

    # Ссылка Забыл пароль"""
    link_forgot_pass = WebElement(id="forgot_password")

    # Поля ввода email и пароль"""
    field_mail = WebElement(id="username")
    field_pass = WebElement(id="password")

    # Кнопка Войти
    button_come_in = WebElement(id="kc-login")

    # Сообщение об ошибке - Неверный логин или пароль
    log_pass_error = WebElement(xpath='//*[@id="page-right"]//p')
    site_ros_telecom = WebElement(id='rt-btn')

    # Имя пользователя в ЛК
    name_user_in_kab = WebElement(xpath='//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/span[2]')


    # СТРАНИЦА РЕГИСТРАЦИИ /////////////////////////////////////////////////

    # Кнопка Зарегистрироваться
    button_reg = WebElement(name="register")

    # Поля ввода имени и фамилии
    field_name = WebElement(name='firstName')
    field_surname = WebElement(name='lastName')

    # Поля ввода email, пароля, подтверждения пароля
    field_reg_email = WebElement(id='address')
    field_reg_pass = WebElement(name="password")
    field_confirm = WebElement(name="password-confirm")

    # Подтверждение отправки кода
    confirmation = WebElement(xpath='//div[@class="card-container__content"]/p')

    # слоган
    tagline = WebElement(id="page-left")

    # Пользователское соглашение и Политика конфиденциальности
    agreement = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[5]/a[1]')
    politic = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[1]')


    # СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ //////////////////////////////////////

    # страница восстановления пароля
    passw_reco = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/h1[1]')