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
    DATA_FOR_INCORRECT_LOGIN = {
        'argnames': 'username,password,comment',
        'argvalues': [
            (' test@test.com', 'Ab12345678', 'Space before login'),
            ('test@test.com ', 'Ab12345678', 'Space after login'),
            ('Ab', 'Ab12345678 ', 'Login 2 symbols'),
            ('   ', 'Ab12345678', 'Login from spaces'),
            ('test@test.com', 'ab12345678', 'Only lower symbols in the password'),
            ('test@test.com', 'AB12345678', 'Only higher symbols in the password '),
            ('test@test.com', '        ', 'Only spaces in the password')
        ]
    }


class RegisterFormLocators:
    DATA_FOR_CORRECT_REGISTER = {
        'argnames': 'username,password,comment',
        'argvalues': [
            ('test@test.com', 'Qwerty12345', 'Correct register data'),
            ('abc', 'Qwerty12345', 'Login 3 symbols'),
            ('qwertyuiopasdfghjklzxcvbnmqwertyuiopasdf', 'Qwerty12345', 'Login 40 symbols'),
            ('test@test.com', 'Ab123456', 'Password 8 symbols'),
            ('test@test.com', 'Ab123456789123456789', 'Password 20 symbols')
        ]
    }
    REGISTER_FORM_EMAIL = (By.ID, 'userNameOnRegister')
    REGISTER_FORM_PASSWORD = (By.ID, 'passwordOnRegister')
    REGISTER_FORM_BUTTON_TO_REGISTER = (By.ID, 'register')
    REGISTER_FORM_BUTTON_TO_BACK = (By.ID, 'backOnRegister')
    REGISTER_TITLE = (By.ID, 'registerForm')
    REGISTER_MESSAGE = (By.ID, 'errorMessageOnRegister')
