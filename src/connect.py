'''
Get specific information from the site.
'''
import chromedriver_binary  # noqa: F401 # pylint: disable=W0611
from selenium import webdriver, common


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

    def get(self) -> str:
        '''
        Get the information of the cancellation and supplementary from UNIPA.

        Returns:
            str: A character string containing the information on
                 the acquired class cancellation and supplementary.
        '''
        browser = self.browser

        try:
            browser.get(self.url)
        except common.exceptions.TimeoutException():
            print('Time out.')
            return ''

        user_id_from = browser.find_element_by_id('loginForm:userId')
        user_id_from.send_keys(self.user_id)
        password_form = browser.find_element_by_id('loginForm:password')
        password_form.send_keys(self.password)

        login_button = browser.find_element_by_id('loginForm:loginButton')
        login_button.click()

        canceled_class_information = browser.find_element_by_id(
            'funcForm:tabArea:0:j_idt232:1:j_idt233').text
        print('Success. Acquisition completed.')
        return canceled_class_information

    def __exit__(self, url: str, user_id: str, password: str) -> None:
        '''
        Terminate the connection.
        '''
        print('del: browser...')
        self.browser.quit()
