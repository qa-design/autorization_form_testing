from selenium.webdriver.common.by import By

URL = 'https://anatoly-karpovich.github.io/HiqoMeetup/'


class LoginFormLocators:
    LOGIN_FORM_EMAIL = (By.ID, 'userName')
    LOGIN_FORM_PASSWORD = (By.ID, 'password')
    LOGIN_FORM_SUBMIT = (By.ID, 'submit')
    LOGIN_FORM_CHANGE_TO_REGISTER = (By.ID, 'registerOnLogin')
    LOGIN_TITLE = (By.ID, 'loginForm')
    LOGIN_SUCCESS_MESSAGE = (By.ID, 'successMessage')
    LOGIN_FORM_INVALID_MESSAGE = (By.ID, 'errorMessage')
    DATA_FOR_LOGIN = {
        'argnames': 'username,password,comment',
        'argvalues': [
            ('Ab', '12345678', 'Space before login'),
            ('Abc ', '12345678', 'Space after login')
        ]
    }


class RegisterFormLocators:
    DATA_FOR_REGISTER = {
        'argnames': 'username,password,comment',
        'argvalues': [
            ('test1@test.com', 'Qwerty12345', 'Correct register data'),
        ]
    }
    REGISTER_FORM_EMAIL = (By.ID, 'userNameOnRegister')
    REGISTER_FORM_PASSWORD = (By.ID, 'passwordOnRegister')
    REGISTER_FORM_BUTTON_TO_REGISTER = (By.ID, 'register')
    REGISTER_FORM_BUTTON_TO_BACK = (By.ID, 'backOnRegister')
    REGISTER_TITLE = (By.ID, 'registerForm')
    REGISTER_MESSAGE = (By.ID, 'errorMessageOnRegister')
