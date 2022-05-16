import locators
from locators import LoginFormLocators
from locators import RegisterFormLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


class LoginForm(BasePage):
    def input_data_to_login_form(self, username, password):
        self.browser.find_element(*LoginFormLocators.LOGIN_FORM_EMAIL).send_keys(username)
        self.browser.find_element(*LoginFormLocators.LOGIN_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginFormLocators.LOGIN_FORM_SUBMIT).click()

    def check_invalid_login(self, comment):
        assert self.browser.find_element(*LoginFormLocators.LOGIN_FORM_INVALID_MESSAGE), comment

    def check_valid_login(self, username, comment):
        assert f'Hello, {username}' in self.browser.find_element(*LoginFormLocators.LOGIN_SUCCESS_MESSAGE).text, \
            comment

    def should_be_login_form(self):
        assert self.browser.current_url == locators.URL
        assert "Login" == self.browser.find_element(*LoginFormLocators.LOGIN_TITLE).text, 'This is not a login form'

    def should_be_register_form(self):
        assert self.browser.current_url == locators.URL
        assert "Registration" == self.browser.find_element(*RegisterFormLocators.REGISTER_TITLE).text, \
            'This is not a register form'

    def go_to_register_form(self):
        self.browser.find_element(*LoginFormLocators.LOGIN_FORM_CHANGE_TO_REGISTER).click()


class RegisterForm(BasePage):
    def check_for_correct_register(self, comment):
        assert 'Successfully registered!' in self.browser.find_element(*RegisterFormLocators.REGISTER_MESSAGE).text,\
            comment

    def check_for_incorrect_register(self, comment):
        assert 'Successfully registered!' not in self.browser.find_element(*RegisterFormLocators.REGISTER_MESSAGE).text, \
            comment

    def go_to_login_form(self):
        back = self.browser.find_element(*RegisterFormLocators.REGISTER_FORM_BUTTON_TO_BACK)
        back.click()

    def input_data_for_register_form(self, username, password):
        self.browser.find_element(*RegisterFormLocators.REGISTER_FORM_EMAIL).send_keys(username)
        self.browser.find_element(*RegisterFormLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*RegisterFormLocators.REGISTER_FORM_BUTTON_TO_REGISTER).click()
