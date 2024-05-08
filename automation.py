# https://digital.banquemisr.com/bmonlinebusiness/customer-login



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteAutomator:
    def __init__(self, error_signal):
        options = Options()
        self.error_signal = error_signal
        options.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
        options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script


        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def load_website(self, url):
        self.driver.get(url)
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def check_element(self, element_id):
        try:
            element_present = EC.presence_of_element_located((By.ID, element_id))
            self.wait.until(element_present)
            return True
        except:
            return False

    def close(self):
        # Do not quit the driver here; let the user close it manually
        pass

class BankMisrAutomator(WebsiteAutomator):
    url = 'https://digital.banquemisr.com/bmonlinebusiness/'
    def __init__(self, error_signal):
        super().__init__(error_signal)
        self.load_website(self.url)
        

    def login(self, username, password):
        # Wait for the username field to be present and enter the username
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        username_field.send_keys(username)

        # Wait for the password field to be present and enter the password
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys(password)

        # Wait for the login button to be present and click it
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        login_button.click()

        error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-main/div/div[2]/app-customer-login/div/div/div[1]/div[1]/form/div/div/div[2]/div[3]/div')))
        
        # if error_message:
        # self.error_signal.error_occurred.emit(str(error_message.text))
        ## here
        # wait until page load
        # login_button = self.wait.until(EC.url_to_be(self.url + "new-url"))
