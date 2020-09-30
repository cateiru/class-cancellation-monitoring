'''
@author: Yuto Watanabe <yuto.w51942@gmail.com>

Copyright (c) 2019-2020 Yuto Watanabe
'''
from selenium import common, webdriver


class ConnectWeb():
    '''
    Obtain information on canceled and supplementary classes from UNIPA.
    '''

    def __init__(self, url: str, user_id: str, password: str) -> None:
        '''
        Class initialization.

        Args:
            user_id (str): Student ID number to log in to UNIPA.
            password (str): Password to log in to UNIPA.
        '''
        self.user_id = user_id
        self.password = password
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.browser.set_page_load_timeout(20)

    def __enter__(self):
        '''
        enter
        '''
        return self

    def login(self) -> str:
        '''
        login to `UNIPA`.

        Returns:
            str: system message.
        '''
        self.browser

        try:
            self.browser.get(self.url)
        except common.exceptions.TimeoutException():
            # time out
            return 'Error: request timed out.'

        user_id_from = self.browser.find_element_by_id('loginForm:userId')
        user_id_from.send_keys(self.user_id)
        password_form = self.browser.find_element_by_id('loginForm:password')
        password_form.send_keys(self.password)

        login_button = self.browser.find_element_by_id('loginForm:loginButton')
        login_button.click()

        return 'Success: opened.'

    def get_teach(self) -> str:
        '''
        Notice from faculty members

        Returns:
            str: Obtained information.
        '''

        canceled_class_information = self.browser.find_element_by_id(
            'funcForm:tabArea:0:j_idt232:0:j_idt233').text

        return canceled_class_information

    def get_cancel(self) -> str:
        '''
        Cancellation / supplementary class / classroom change

        Returns:
            str: Obtained information.
        '''

        canceled_class_information = self.browser.find_element_by_id(
            'funcForm:tabArea:0:j_idt232:1:j_idt233').text

        return canceled_class_information

    def get_class(self) -> str:
        '''
        Notice about class.

        Returns:
            str: Obtained information.
        '''

        canceled_class_information = self.browser.find_element_by_id(
            'funcForm:tabArea:0:j_idt232:2:j_idt233').text

        return canceled_class_information

    def get_life(self) -> str:
        '''
        Notice about school life in general.

        Returns:
            str: Obtained information.
        '''

        canceled_class_information = self.browser.find_element_by_id(
            'funcForm:tabArea:0:j_idt232:3:j_idt233').text

        return canceled_class_information

    def __exit__(self, url: str, user_id: str, password: str) -> str:
        '''
        Terminate the connection.
        '''
        self.browser.quit()
        return 'Success: closed.'
