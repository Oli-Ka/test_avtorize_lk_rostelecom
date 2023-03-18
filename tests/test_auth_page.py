import time
import pytest
from pages.auth_page import AuthPage
from config import valid_email, valid_email2, valid_password, phone, negative_email, negative_email2, negative_phone, negative_pass, name, name2, name3, name4, name5, surname


# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py


def test_1_reg_new_user_poz(selenium):
    '''Позитивный тест для регистрации нового пользователя, и перехода на
    страницу подтверждения почты'''
    page = AuthPage(selenium)
    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password)
    page.field_confirm.send_keys(valid_password)
    page.button_reg.click()
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()


@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_2_reg_new_user_name_neg(selenium):
    '''Негативный тест (Имя из буквы кириллицы и -) для регистрации нового
    пользователя'''
    page = AuthPage(selenium)
    page.link_register.click()
    page.field_name.send_keys(name2)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password)
    page.field_confirm.send_keys(valid_password)
    time.sleep(2)
    page.button_reg.click()
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()

@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_3_reg_new_user_name_neg2(selenium):
    '''Негативный тест (Имя из 31 буквы) для регистрации нового
    пользователя'''
    page = AuthPage(selenium)
    page.link_register.click()
    page.field_name.send_keys(name3)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password)
    page.field_confirm.send_keys(valid_password)
    time.sleep(2)
    page.button_reg.click()
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()

@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_4_reg_new_user_name_neg3(selenium):
    '''Негативный тест (Имя из символов латиницы) для регистрации нового
    пользователя'''
    page = AuthPage(selenium)
    page.link_register.click()
    page.field_name.send_keys(name4)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password)
    page.field_confirm.send_keys(valid_password)
    page.button_reg.click()
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()


@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_5_reg_new_user_name_neg4(selenium):
    '''Негативный тест (Имя из спецзнаков) для регистрации нового
    пользователя'''
    page = AuthPage(selenium)
    page.link_register.click()
    page.field_name.send_keys(name5)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password)
    page.field_confirm.send_keys(valid_password)
    page.button_reg.click()
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()


@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_6_reg_new_user_email_neg(selenium):
    '''Негативный тест (почта без @) для регистрации нового
    пользователя, и перехода на страницу подтверждения почты'''
    page = AuthPage(selenium)
    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(negative_email2)
    page.field_reg_pass.send_keys(valid_password)
    page.field_confirm.send_keys(valid_password)
    page.button_reg.click()
    time.sleep(2)
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()


def test_7_reg_new_user_link_change_mail_poz(selenium):
    '''Позитивный тест о присутствии ссылки для изменения почты на этапе
    получения кода, после нажатия кнопки "зарегистрироваться"'''
    page = AuthPage(selenium)
    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password)
    page.field_confirm.send_keys(valid_password)
    page.button_reg.click()
    time.sleep(2)
    assert 'Изменить email' in page.link_change_mail.get_text()


def test_8_auth_user_email_poz(selenium):
    '''Позитивный тест, проверяет обычную авторизацию по электронной почте
    с валидными данными'''
    page = AuthPage(selenium)
    page.field_mail.send_keys(valid_email)
    page.field_pass.send_keys(valid_password)
    page.button_come_in.click()
    if page.name_user_in_kab.is_presented():
        assert True
    else:
        assert False


@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_9_auth_user_email_neg(selenium):
    '''Негативный тест, проверяет обычную авторизацию по электронной почте
    с несуществующей почтой'''
    page = AuthPage(selenium)
    page.field_mail.send_keys(negative_email)
    page.field_pass.send_keys(valid_password)
    page.button_come_in.click()
    if page.name_user_in_kab.is_presented():
        assert True
    else:
        assert False


def test_10_auth_user_phone_poz(selenium):
    '''Позитивный тест, проверяет обычную авторизацию по номеру телефона
    с валидными данными'''
    page = AuthPage(selenium)
    page.field_mail.send_keys(phone)
    page.field_pass.send_keys(valid_password)
    page.button_come_in.click()
    if page.name_user_in_kab.is_presented():
        assert True
    else:
        assert False


@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_11_auth_user_phone_neg(selenium):
    '''Негативный тест, проверяет обычную авторизацию по номеру телефона
    с неверным номером'''
    page = AuthPage(selenium)
    page.field_mail.send_keys(negative_phone)
    page.field_pass.send_keys(valid_password)
    page.button_come_in.click()
    if page.name_user_in_kab.is_presented():
        assert True
    else:
        assert False


def test_12_passw_reco_poz(selenium):
    '''Позитивный тест для проверки перехода на страницу восстановления
    пароля'''
    page = AuthPage(selenium)
    page.link_forgot_pass.click()
    assert "Восстановление пароля" in page.passw_reco.get_text()


@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_13_tagline(selenium):
    ''' Проверка наличия продуктового слогана в левом блоке страницы
    регистрации'''
    page = AuthPage(selenium)
    page.link_register.click()
    assert "Персональный помощник в цифровом мире Ростелекома" in page.tagline.get_text()


def test_14_link_agreement_poz(selenium):
    '''Позитивный тест для проверки наличия ссылки на пользовательское
    соглашение'''
    page = AuthPage(selenium)
    page.link_register.click()
    assert 'пользовательского соглашения' in page.agreement.get_text()

@pytest.mark.xfail(reason="Здесь XFAIL - норма (т.к. тест негативный), PASS - Баг!!!")
def test_15_link_agreement_poz(selenium):
    '''Негативный тест для проверки, что при переходе по ссылке в футере
    "Политикой конфиденциальности", открывается страница Пользовательского
    соглашения'''
    page = AuthPage(selenium)
    page.politic.click()
    time.sleep(5)
    assert page.get_current_url() != 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py