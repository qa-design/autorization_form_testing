import pytest
import locators
from form import LoginForm
from form import RegisterForm


@pytest.mark.parametrize(**locators.RegisterFormLocators.DATA_FOR_REGISTER)
def test_correct_login_data(browser, username, password, comment):
    page = LoginForm(browser, locators.URL)
    page.open()
    page.go_to_register_form()
    register_form = RegisterForm(browser, browser.current_url)
    register_form.input_data_for_register_form(username, password)
    register_form.check_for_correct_register(comment)
    register_form.go_to_login_form()
    page.input_data_to_login_form(username, password)
    page.check_valid_login(username, comment)


@pytest.mark.parametrize(**locators.RegisterFormLocators.DATA_FOR_REGISTER)
def test_correct_register(browser, username, password, comment):
    page = LoginForm(browser, locators.URL)
    page.open()
    page.go_to_register_form()
    register_form = RegisterForm(browser, browser.current_url)
    register_form.input_data_for_register_form(username, password)
    register_form.check_for_correct_register(comment)


@pytest.mark.parametrize(**locators.LoginFormLocators.DATA_FOR_LOGIN)
def test_incorrect_login_data(browser, username, password, comment):
    page = LoginForm(browser, locators.URL)
    page.open()
    page.input_data_to_login_form(username, password)
    page.check_invalid_login(comment)


def test_should_be_login_form(browser):
    page = LoginForm(browser, locators.URL)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    page = LoginForm(browser, locators.URL)
    page.open()
    page.go_to_register_form()
    page.should_be_register_form()
