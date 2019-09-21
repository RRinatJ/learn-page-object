from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)
            
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        
    def webdriver_wait_element(self, time, how, what):
        try:
            WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located((how, what))
            )
        except (TimeoutException):
            return False
        return True
        
    def webdriver_wait_alert(self, time):
        try:
            WebDriverWait(self.browser, time).until(
            EC.alert_is_present()
            )    
        except (TimeoutException):
            return False
        return True
        
    def solve_quiz_and_get_code(self):         
        self.webdriver_wait_alert(5)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")